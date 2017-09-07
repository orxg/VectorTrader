# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 08:43:43 2017

@author: ldh

定义关于数据的api.
"""

# api_data.py

from VectorTrader.data.data_source.mixed_data_source.mixed_data_source import MixedDataSource

mixed_data_source = MixedDataSource()

def get_stocks_basics(ticker_list):
    '''
    获取股票基本信息。包括其所属行业，行业指数代码。
    '''
    return mixed_data_source.get_stocks_basics(ticker_list)

def get_industry_factors(industry_wind_id, field, start_date, end_date):
    '''
    获取行业指数所属行业的信息，如行业算数平均PE.
    '''
    return mixed_data_source.get_industry_factors(industry_wind_id,field,
                                                  start_date, end_date)

def get_stock_factors(ticker, field, start_date, end_date):
    '''
    获取股票因子数据。
    '''
    return mixed_data_source.get_stock_factors(ticker,field,
                                               start_date, end_date)
    
def get_stock_factors_with_industry(ticker,field,start_date,end_date):
    '''
    获取股票因子数据附带对应行业数据。
    '''
    return mixed_data_source.get_stock_factors_with_industry(ticker,field,
                                                             start_date,end_date)
