# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:08:35 2017

@author: ldh 
"""

# history_bars.py

# --------------------------Abandon-----------------------------
from ..events import EVENT
from ..utils.convertor import dataframe_to_bars,bars_to_dataframe

class HistoryBars():
    '''
    historic available data during the running process.提供高效的可得行情数据接口。
    '''
    def __init__(self,env,ini_window):
        '''
        Parameters
        -----------
            env
                环境
            ini_window
                初始化历史数据长度
        '''
        self._env = env
        self.ini_window = ini_window
        self.event_bus = self._env.event_bus
        self._history_bars = {}
        self._init_history_bars()
        self.event_bus.add_listener(EVENT.POST_BAR,self._update_post_bar)
        
    def _init_history_bars(self):
        start_date = self._env.start_date
        calendar = self._env.calendar
        end_date = calendar.adjust_date(start_date,-1).strftime('%Y%m%d')
        adjusted_start_date = calendar.adjust_date(start_date,-self.ini_window).strftime('%Y%m%d')
        frequency = self._env.frequency
        for ticker in self._env.universe:
            ini_data = self._env.data_proxy.get_history(ticker,
                              adjusted_start_date,
                              end_date,
                              frequency,'-1')
            ini_bars = dataframe_to_bars(ini_data,ticker,frequency)
            self._history_bars[ticker] = ini_bars
            
    def _update_post_bar(self,event):
        bar_map = self._env.bar_map
        for ticker in self._env.universe:
            new_bar = bar_map[ticker]
            self._history_bars[ticker].append(new_bar)
    
    def get_history(self,n):
        '''
        获取以当前bar为基准的过去n个bar的交易数据。不含当前bar.全universe.
        '''
        history = {}
        for ticker in self._env.universe:
            bars = self._history_bars[ticker][-n:]
            df = bars_to_dataframe(bars)
            history[ticker] = df
        return history
            
        
        
    
    
    
    
    
    
    
    
    
    
    
            