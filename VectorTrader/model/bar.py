# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:56:35 2017

@author: ldh
"""

# bar.py

from collections import defaultdict
from ..events import EVENT

class BarMap():
    def __init__(self,env):
        '''
        为Strategy,Account,Broker提供bar数据。
        是系统内部数据的传递者,其数据来自于data_proxy.
        '''
        self._data = defaultdict(list)
        self.env = env        
        self.env.event_bus.add_listener(EVENT.PRE_BAR,self._update_pre_bar)
        
    def __str__(self):
        return str(self._data)
    
    def _update_pre_bar(self,event):
        data_proxy = self.env.data_proxy
        for ticker in self.env.universe:
            self._data[ticker].append(data_proxy.get_bar(ticker))
        
    def __getitem__(self,ticker):
        return self._data[ticker]
    
    def get_latest_bar(self,ticker):
        try:
            return self._data[ticker][-1]
        except:
            return None
        
    def get_latest_bar_value(self,ticker,val_type = 'close_price'):
        '''
        获取最近的bar的某个属性值。
        '''
        return self._data[ticker][-1][1][val_type]
    
# ------------------------------ Abandon -------------------------------
class Bar():
    def __init__(self,dt,ticker,frequency):
        '''
        约定的基本数据结构。
        DataProxy所返回的基本数据结构之一,用于回测/模拟/实盘。由DataProxy实现。        
        
        Parameters
        -------------
            dt
                datetime
            ticker
                股票代码
            frequency
                '1d','1m','5m',...
                
        '''
        self._dt = dt
        self._ticker = ticker
        self._frequency = frequency
        self.open_price = None
        self.high_price = None
        self.low_price = None
        self.close_price = None
        self.volume = None
        
        self._prev_close = None
        self._is_halt = None
        self._limit_up = None
        self._limit_down = None
        self._dividend = None
        self._split = None
        
    @property
    def ticker(self):
        return self._ticker
    
    @property
    def date_time(self):
        return self._dt
    
    @property
    def frequency(self):
        return self._frequency   
    
    @property
    def open_price(self):
        return self._data['open_price']
    
    @property
    def high_price(self):
        return self._data['high_price']
    
    @property
    def low_price(self):
        return self._data['low_price']
    
    @property
    def close_price(self):
        return self._data['close_price']
    
    @property
    def volume(self):
        return self._data['volume']  
     
    @property
    def limit_up(self):
        return self._limit_up
    
class Bars():
    def __init__(self,ticker,frequency):
        '''
        约定的基本数据结构。
        DataProxy所返回的基本数据结构之一,用于回测/模拟/实盘。由DataProxy实现。        
        
        Parameters
        -------------
            ticker
                股票代码
            _type
                '1d','1m','5m',...
                
        Attributes
        -------------
            _data
                DataFrame(date_time,open_price,high_price,low_price,close_price,volume)
            _limit_up
                DataFrame(date_time,limit_up,limit_up_price)
            _limit_down
                DataFrme(date_time,limit_down,limit_down_price)
            _is_halt
                DataFrme(date_time,is_halt)    
        '''
        self._ticker = ticker
        self._frequency = frequency
        self._start_date = None
        self._end_date = None
        self._data = None
        self._prev_close = None
        self._is_halt = None
        self._limit_up = None
        self._limit_down = None
        self._dividend = None
        self._split = None
        
    @property
    def ticker(self):
        return self._ticker
    
    @property
    def frequency(self):
        return self.frequency
    
    @property
    def start_date(self):
        return self._start_date
    
    @property
    def end_date(self):
        return self._end_date    
    
    @property
    def open_price(self):
        return self._data['open_price']
    
    @property
    def high_price(self):
        return self._data['high_price']
    
    @property
    def low_price(self):
        return self._data['low_price']
    
    @property
    def close_price(self):
        return self._data['close_price']
    
    @property
    def volume(self):
        return self._data['volume']  
     
    @property
    def limit_up(self):
        return self._limit_up        
        
    

