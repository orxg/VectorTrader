# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:12:48 2017

@author: ldh
"""

# data_proxy.py
from ..environment import Environment
from ..module.bar import Bar

class DataProxy():
    '''
    对不同类型的data_source的封装。计划支持不同模式下的代理。
    对于回测/模拟/实盘实现一套系统内部的数据结构，并定义接口。
    对于研究而言，实现以DataFrame为基准的数据结构的接口。
    
    这样的好处在于DataSource只需要实现DataFrame数据类型。
    DataProxy负责对DataFrame数据类型进行加工得到定义的数据类型。
    '''
    
    def __init__(self,data_source,mode = 'b'):
        self.data_source = data_source 
        self._bars_map = None
        self.mode = mode
        
        if self.mode == 'b':
            # 回测模式
            self._initilize_backtest_data()

        elif self.mode == 'p':
            # 模拟模式
            pass
        elif self.mode == 'r':
            # 实盘
            pass
        elif self.mode == 's':
            # 研究
            pass
        
    def _initilize_backtest_data(self):
        '''
        准备数据.
        '''        
        env = Environment.get_instance()
        universe = env.universe
        start_date = env.start_date
        end_date = env.end_date
        frequency = env.frequency
        
        # 回测专有数据
        self._data = None
        self._calendar_days = None
        
        self._calendar_days = self.data_source.get_calendar_days(start_date,
                                                                 end_date)
        for ticker in universe:
            self._data[ticker] = self.data_source.get_history(
                                                    ticker,
                                                    start_date,
                                                    end_date,
                                                    frequency)
                   
    ## 回测/模拟/实盘 数据接口
    def get_bar(self,dt,ticker,frequency):
        ## XXX: 效率似乎不高，总是执行loc
        if self.mode == 'b':
            bar = Bar(dt,ticker,frequency)
            price_board = self._data[ticker].loc[dt]
            bar.close_price = price_board['close_price']
            bar.open_price = price_board['open_price']
            bar.high_price = price_board['high_price']
            bar.low_price = price_board['low_price']
            bar.volume = price_board['volume']
            return bar
                                     
    def get_history(self,ticker,start_date,end_date,frequency):
        '''
        数据接口。
        '''
        return self.data_source.get_history(ticker,start_date,end_date,frequency)
            
    def get_calendar_days(self,start_date,end_date):
        '''
        返回start_date到end_date间的交易日。
        Return
        -------
            list [pd.Timestamp]
        '''
        if self.mode == 'b':
            return self._calendar_days[start_date:end_date].tolist()
        else:
            calendar_days = self.data_source.get_calendar_days(start_date,
                                                               end_date)
            return calendar_days.tolist()
        

    