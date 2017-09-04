# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:52:45 2017

@author: LDH
"""

# analyser.py
import pickle
import datetime
import pandas as pd
import seaborn as sns

from ..events import EVENT
from ..utils.stats import calc_bar_return,calc_return_pnl
class Analyser():

    def __init__(self,env):
        self.env = env
        
        self.portfolio_net_value = []
        self.position_record = []        
        self.env.event_bus.add_listener(EVENT.POST_BAR,self._record_post_bar)
        if self.env.mode == 'p':
            self.env.event_bus.add_listener(EVENT.POST_SETTLEMENT,self._show_post_settlement)
        
    def get_state(self):
        return pickle.dumps({'portfolio_net_value':self.portfolio_net_value,
                 'position_record':self.position_record})
        
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
        print '******' * 10
        for name,value in self.report.items():
            print name
            print value
            print '******' * 10
        
    def stats(self,name = None,path = None):
        '''
        回测结束后调用该函数，用于统计回测结果。
        parameters
        ------------
            name
                结果名称
            path
                回测结果保存路径
        '''
        # 存储设定
        if name is None:
            name = 'strategy_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        if path is None:
            path = 'G:\\Work_ldh\\Backtest\\VectorTrader\\out\\'
        
        out_path = path + name + '.pkl'
        
        # 资金曲线
        self.portfolio_value = pd.DataFrame(self.portfolio_net_value,
                                            columns = ['trading_dt',
                                                       'total_asset_value']).set_index('trading_dt')
        self.bar_return = calc_bar_return(self.portfolio_value['total_asset_value'])
        self.return_pnl = calc_return_pnl(self.portfolio_value['total_asset_value'])
        
        # 订单记录
        self.order_passed = pd.DataFrame(self.env.account.order_passed,columns = ['calendar_dt',
                                                                                   'trading_dt',
                                                                                   'ticker',
                                                                                   'amount',
                                                                                   'direction',
                                                                                   'match_price'])
        self.order_canceled = pd.DataFrame(self.env.account.order_canceled,columns = ['calendar_dt',
                                                                                      'trading_dt',
                                                                                      'ticker',
                                                                                      'amount',
                                                                                      'reason'])
        
        # 存储
        report = {}
        report['bar_return'] = self.bar_return
        report['return_pnl'] = self.return_pnl
        report['order_passed'] = self.order_passed
        report['order_canceled'] = self.order_canceled
        
        with open(out_path,'w') as f: 
            pickle.dump(report,f)
        self.report = report
        
    def show_stats(self):
        '''
        展示回测统计结果。
        '''
        sns.set_style('dark')
        print self.order_passed
        print self.order_canceled
        self.return_pnl.plot(figsize = (20,8))
        
    
    
    