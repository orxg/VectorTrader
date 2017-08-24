# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:06:03 2017

@author: ldh
"""

# api_wind.py

import datetime as dt

import pandas as pd
import numpy as np
from WindPy import *
import tushare as ts

from utils import symbol_convertor_wind

w.start()


def get_all_symbols():
    '''
    返回全A股的股票代码。
    Returns
    ----------
        list
    '''
    symbols = ts.get_stock_basics().index.tolist()
    return symbols

def get_trading_days(start_date,end_date):
    trading_days = w.tdays(start_date, end_date, "")
    trading_days = pd.Series(trading_days.Data[0])
    return trading_days


def get_basics(ticker,add_ticker = True):
    '''
    获取单只股票的基本信息。
    Return
    ---------
        DataFrame
    '''
    current_date = dt.date.today().strftime('%Y-%m-%d')
    wind_ticker = symbol_convertor_wind(ticker)
    basics = w.wsd(wind_ticker, 
          "sec_name,ipo_date,total_shares,float_a_shares,industry_gics,industry_gicscode,indexcode_wind",
          "ED0D", current_date , "industryType=2;unit=1;PriceAdj=F")
    basics_df = pd.DataFrame(basics.Data,index = basics.Fields,columns = [ticker]).T
    
    names = basics.Fields
    new_names = []
    for each in names:
        new_names.append(each.lower())
    columns = {}
    for idx,each in enumerate(names):
        columns[each] = new_names[idx]
    
    basics_df = basics_df.rename(columns = columns)
    if add_ticker == True:
        basics_df['ticker'] = ticker
    return basics_df

def get_stock_list_basics(ticker_list):
    '''
    获取股票列表的基本信息。
    Parameters
    -----------
        ticker_list
            ['600340','000001']
    Returns
    ----------
        DataFrame
    '''
    current_date = dt.date.today().strftime('%Y%m%d')
    wind_ticker_list = []
    for each in ticker_list:
        wind_ticker_list.append(symbol_convertor_wind(each))
    
    data = w.wss(wind_ticker_list,
          "sec_name,ipo_date,total_shares,float_a_shares,free_float_shares,industry_gics,industry_gicscode,indexcode_wind",
          "industryType=2;tradeDate=%s;unit=1"%current_date)
    data_df = pd.DataFrame(data.Data,index = data.Fields,columns = data.Codes).T
    
    names = data.Fields
    new_names = []
    for each in names:
        new_names.append(each.lower())
    columns = {}
    for idx,each in enumerate(names):
        columns[each] = new_names[idx]
    data_df = data_df.rename(columns = columns)
    data_df['ticker'] = ticker_list
    return data_df

def get_stock_daily_price(ticker,start_date,end_date,add_ticker = True,
                          add_time = True):
    '''
    获取指定股票日间交易数据。ticker支持非wind代码。内部会对其进行处理。
    只支持单只股票。
    Parameters
    ----------
        ticker
            股票代码
        start_date
            '20150101'
        end_date
        
    Retruns
    --------
        DataFrame
            index:time
            columns:open_price,high_price,low_price,close_price,volume,amount,
                    free_turnover_ratio,trade_status,maxup_or_maxdown
    '''
    wind_ticker = symbol_convertor_wind(ticker)
        
    data = w.wsd(wind_ticker, 
          "open,high,low,close,volume,amt,free_turn,trade_status,maxupordown", 
          start_date, end_date, "PriceAdj=F")
    data_df = pd.DataFrame(np.mat(data.Data).T,index = data.Times,columns = data.Fields)
    columns = 'open_price,high_price,low_price,close_price,volume,amount,free_turnover_ratio,trade_status,maxup_or_maxdown'.split(',')
    columns_dict = {}    
    for idx,name in enumerate(data_df.columns.tolist()):
        columns_dict[name] =columns[idx]       
    data_df = data_df.rename(columns = columns_dict)
    
    if add_ticker == True:
        data_df['ticker'] = ticker
    if add_time == True:
        data_df['date_time'] = data_df.index
        
    return data_df

def get_factors():
    '''
    获取因子数据。
    '''
    pass

if __name__ == '__main__':
    bas = get_trading_days('2010-01-01','2015-01-01')