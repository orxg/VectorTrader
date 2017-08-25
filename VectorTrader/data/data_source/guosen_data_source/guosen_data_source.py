# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:10:15 2017

@author: ldh
"""

# guosen_data_source.py

from VectorTrader.interface import AbstractDataSource

from matlab_utils import get_matlab_symbols,get_matlab_history

class GuosenDataSource(AbstractDataSource):
    
    def __init__(self):
        pass
    
    def get_symbols(self):
        '''
        Returns
        ---------
            list
        '''
        return get_matlab_symbols
    
    def get_history(self,ticker,start_date,end_date,frequency):
        '''
        Returns
        --------
            DataFrame(date_time,open_price,high_price,low_price,close_price,volume)
        '''
        return get_matlab_history(ticker,start_date,end_date,frequency)

    def get_calendar_days(self,start_date,end_date):
        '''
        Returns
        --------
            Series [pd.Timestamp]
        '''
        pass
    
    def get_factor(self,factor,ticker,start_date,end_date):
        '''
        Returns
        --------
            DataFrame
        '''
        pass
    

                

