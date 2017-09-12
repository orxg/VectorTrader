# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:52:45 2017

@author: LDH
"""

# analyser.py
import pickle
import datetime
from collections import OrderedDict
import pandas as pd
import seaborn as sns

from ..events import EVENT
from ..utils.stats import calc_bar_return,calc_return_pnl,\
                        calc_total_return,calc_annul_return,calc_max_drawdown,\
                        calc_sharp_ratio
class Analyser():

    def __init__(self,env,name = None,path = None):
        self.env = env
        self.name = name
        self.path = path
        
        self.portfolio_net_value = []
        self.position_record = []        
        self.env.event_bus.add_listener(EVENT.POST_BAR,self._record_post_bar)
        if self.env.mode == 'p':
            self.env.event_bus.add_listener(EVENT.POST_SETTLEMENT,self._show_post_settlement)
        
    def get_state(self):
        return pickle.dumps({
                'portfolio_net_value':self.portfolio_net_value,
                 'position_record':self.position_record
                 })
        
    def set_state(self,state):
        state = pickle.loads(state)
        self.portfolio_net_value = state['portfolio_net_value']
        self.position_record = state['position_record']
    
    def _record_post_bar(self,event):
        calendar_dt = self.env.calendar_dt
        account = self.env.account
        self.portfolio_net_value.append([calendar_dt,account.total_asset_value])
        self.position_record.append([calendar_dt,account.position.position])
        
    def _show_post_settlement(self,event):
        self.stats()
        self.show_stats()
        
    def stats(self):
        '''
        统计当前时刻的各项指标，生成报告。
        '''
        # 存储设定
        if self.name is None:
            self.name = 'strategy_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        if self.path is None:
            self.path = 'G:\\Work_ldh\\Backtest\\StrategyGo\\out\\'
        
        out_path = self.path + self.name + '.pkl'
        
        # 资金曲线
        self.portfolio_value = pd.DataFrame(self.portfolio_net_value,
                                            columns = ['trading_dt',
                                                       'total_asset_value']).set_index('trading_dt')
        self.bar_return = calc_bar_return(self.portfolio_value['total_asset_value'])
        self.return_pnl = calc_return_pnl(self.portfolio_value['total_asset_value'])
        
        # 指标计算
        ## 总收益率
        self.total_return =calc_total_return(self.portfolio_value['total_asset_value'])
        ## 年化收益率
        self.annul_return = calc_annul_return(self.portfolio_value['total_asset_value'])
        ## SharpRatio
        self.sharp_ratio = calc_sharp_ratio(self.portfolio_value['total_asset_value'])
        ## 最大回撤相关
        max_dd,max_ddd,max_dd_start_date,\
        max_dd_end_date,max_ddd_start_date,\
        max_ddd_end_date = calc_max_drawdown(self.portfolio_value['total_asset_value'])
        
        # 订单记录
        self.order_passed = pd.DataFrame(self.env.account.order_passed,
                                         columns = ['calendar_dt',
                                                    'trading_dt',
                                                    'ticker',
                                                    'amount',
                                                    'direction',
                                                    'match_price'])
        self.order_canceled = pd.DataFrame(self.env.account.order_canceled,
                                           columns = ['calendar_dt',
                                                      'trading_dt',
                                                      'ticker',
                                                      'amount',
                                                      'reason'])
        
        # 存储
        report = {}
        report['PnLs'] = {}
        report['Summary'] = OrderedDict()
        report['Record'] = {}
        
        report['PnLs']['bar_return'] = self.bar_return
        report['PnLs']['return_pnl'] = self.return_pnl
        
        report['Summary']['total_return'] = self.total_return
        report['Summary']['annul_return'] = self.annul_return
        report['Summary']['sharp_ratio'] = self.sharp_ratio
        report['Summary']['max_drawdown'] = max_dd
        report['Summary']['max_drawdown_duration'] = max_ddd
        report['Summary']['max_drawdown_start_date'] = max_dd_start_date
        report['Summary']['max_drawdown_date'] = max_dd_end_date
        report['Summary']['max_drawdown_end_date'] = max_ddd_end_date
        
        report['Record']['order_passed'] = self.order_passed
        report['Record']['order_canceled'] = self.order_canceled
        
        with open(out_path,'w') as f: 
            pickle.dump(report,f)
        self.report = report
        
    def show_stats(self):
        '''
        展示当前统计结果。
        '''
        sns.set_style('dark')
        report_summary_df = pd.Series(self.report['Summary'])
        print report_summary_df
        ax = self.return_pnl.plot(figsize = (20,8))
        y_vals = ax.get_yticks()
        ax.set_yticklabels(['{:3.2f}%'.format(x * 100) for x in y_vals])
        ax.grid(True)
    
    
    