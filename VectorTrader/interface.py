# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 22:32:09 2017

@author: ldh
"""

# interface.py
from abc import ABCMeta,abstractmethod

class AbstractDataSource():
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_history(self,ticker,start_date,end_date,frequency):
        '''
        Returns
        --------
            DataFrame(date_time,open_price,high_price,low_price,close_price,volume)
        '''
        raise NotImplementedError
        
    @abstractmethod
    def get_calendar_days(self,start_date,end_date):
        '''
        Returns
        --------
            Series [pd.Timestamp]
        '''
        raise NotImplementedError
        