# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:12:48 2017

@author: ldh
"""

# data_proxy.py

class DataProxy():
    '''
    对不同类型的data_source的封装。
    '''
    
    def __init__(self,data_source):
        self.data_source = data_source 
        self.daily_trading_data = {}
        
    def load_trading_data(self,universe,
                              start_date,end_date):
        '''
        准备数据.
        '''        
        for ticker in universe:
            self.daily_trading_data[ticker] = self.data_source.get_daily_trading_data(
                                                    ticker,
                                                    start_date,
                                                    end_date)
                                            
    def get_history(self,ticker,start_date,end_date):
        '''
        数据接口。需要先调用self.load_trading_data后才能调用。
        '''
        try:
            return self.daily_trading_data[ticker][start_date:end_date]
        except:
            print('please run load_trading_data first')
            raise
            
    def get_calendar_days(self,start_date,end_date):
        '''
        返回start_date到end_date间的交易日。
        Return
        -------
            list [pd.Timestamp]
        '''
        calendar_days = self.data_source.get_calendar_days(start_date,
                                                           end_date)
        return calendar_days
        
    