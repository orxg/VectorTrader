# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:18:32 2017

@author: ldh
"""

# context.py
import six
import pickle

from ..environment import Environment

class Context():
    '''
    用户策略上下文。负责向策略提供关于当前的信息(不可更改)包括
        股票池
            当前的股票池
        日期
            当前bar的日期，过去一个交易日的日期
        日历
            交易日历对象
        账户
            账户对象, 账户持仓，账户资金，账户总价值
        历史数据
            过去的历史市场行情,dict,key为股票代码,value为DataFrame
            DataFrame (open_price,high_price,low_price,close_price)                
    '''
    def __init__(self):
        self.signal_post_before_trading = None # 盘前信息
    
    def get_state(self):
        state_data = {}
        for key,value in six.iteritems(self.__dict__):
            if key.startswith('_'):
                continue
            try:
                state_data[key] = pickle.dumps(value)
            except:
                print '{} can not be pickled'.format(key)
        return pickle.dumps(state_data)
            
    def set_state(self,state):
        state_data = pickle.loads(state)
        for key,value in six.iteritems(state_data):
            try:
                self.__dict__[key] = pickle.loads(value)
            except:
                print '{} can not be loaded'.format(key)
         
        
    @property
    def universe(self):
        return Environment.get_instance().get_universe()
    
    @property
    def user_universe(self):
        return Environment.get_instance().universe
    
    @property
    def current_date(self):
        return Environment.get_instance().calendar_dt
    
    @property
    def previous_date(self):
        return Environment.get_instance().calendar.adjust_date(self.current_date,-1)
    
    @property
    def account(self):
        return Environment.get_instance().account
    
    @property
    def position(self):
        return Environment.get_instance().account.position
    
    @property
    def cash(self):
        return Environment.get_instance().account.cash
    
    @property
    def total_asset_value(self):
        return Environment.get_instance().account.total_asset_value
    
    def get_history(self,n):
        '''
    		返回过去N日的前复权数据。
    		'''
        env = Environment.get_instance()
        previous_date = self.previous_date
        history = {}
        for ticker in env.universe:
            history[ticker] = env.data_proxy.get_bars(ticker,n,previous_date)
        return history

            
    
    
    
    
    
