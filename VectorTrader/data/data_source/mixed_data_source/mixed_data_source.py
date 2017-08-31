# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 13:31:10 2017

@author: ldh

混合数据源:
    1. Guosen本地dll数据
    2. Wind接口数据
    3. tushare数据
    4. Guosen本地数据库数据
后续集成数据源在对应的_utils中定义。
"""

# mixed_data_source.py

from VectorTrader.interface import AbstractDataSource

import tushare_utils
import matlab_utils
import wind_utils
import guosen_utils

class MixedDataSource(AbstractDataSource):
    
    def __init__(self):
        pass
    
    def get_symbols(self):
        '''
        获取全A历史股票代码。
        下一步支持板块，支持概念，支持停牌退市，支持按时间段选取。
        Returns
        ---------
            list
        '''
        return matlab_utils.get_matlab_symbols()
    
    def get_history(self,ticker,start_date,end_date,frequency,kind):
        '''
        获取单只股票交易行情。
        Returns
        --------
            DataFrame(date_time,open_price,high_price,low_price,close_price,volume)
        '''
        return matlab_utils.get_matlab_history(ticker,start_date,end_date,
                                               frequency,kind)

    def get_calendar_days(self,start_date,end_date):
        '''
        Returns
        --------
            Series [pd.Timestamp]
        '''
        return tushare_utils.get_calendar_days(start_date,end_date)
    
    def get_basics(self,ticker):
        '''
        获取单只股票基本信息。
        '''
        return wind_utils.get_basics(ticker)
    
    def get_stocks_basics(self,ticker_list):
        '''
        获取多只股票基本信息。
        Returns
        -------
            DataFrame
        '''
        return wind_utils.get_stock_list_basics(ticker_list)
    
    def get_dividend(self,ticker,start_date,end_date):
        '''
        分红送股。
        '''
        return guosen_utils.get_dividend(ticker,start_date,end_date)
    
    def get_rights_issue(self,ticker,start_date,end_date):
        '''
        配股转配股。
        '''
        return guosen_utils.get_rights_issue(ticker,start_date,end_date)
    
    def get_trade_status(self,ticker,start_date,end_date):
        '''
        交易状态。
        '''
        return guosen_utils.get_trade_status(ticker,start_date,end_date)
    
    def get_list_delist_date(self,ticker):
        '''
        上市日期，退市日期。
        '''
        return guosen_utils.get_list_delist_date(ticker)
    
    def get_factor(self,factor,ticker,start_date,end_date):
        '''
        Returns
        --------
            DataFrame
        '''
        pass
    
    def get_industry_factor(self,industry_wind_index,start_date,end_date):
        '''
        获取行业因子数据。
        数据来自Wind.
        '''
        pass
    