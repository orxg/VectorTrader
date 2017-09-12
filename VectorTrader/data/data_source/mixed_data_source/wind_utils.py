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

from utils import wind_symbol_convert,wind_symbol_back_convert,\
                    datetime_format_convertor

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


def get_basics(ticker,industry_type = 2,add_ticker = True):
    '''
    获取单只股票的基本信息。
    
    Parameters
    ----------
    ticker
        股票代码
    industry_type
        返回的行业级别，默认为2级行业
    add_ticker
        是否在结果中添加ticker
    Return
    ---------
    DataFrame
    '''
    current_date = dt.date.today().strftime('%Y-%m-%d')
    wind_ticker = wind_symbol_convert(ticker)
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
        wind_ticker_list.append(wind_symbol_convert(each))
    
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
        '20160101'
    Retruns
    --------
        DataFrame
            index:time
            columns:open_price,high_price,low_price,close_price,volume,amount,
                    free_turnover_ratio,trade_status,maxup_or_maxdown
    '''
    wind_ticker = wind_symbol_convert(ticker)
        
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


    
def get_suspends(trade_date):
    '''
    获取停牌股票集。返回指定日期所有停牌股票。
    		
    Parameters
    -----------
		trade_date
			'20100101'
    Returns
    ---------
    list 
        [ticker,....]
    '''     
    trade_date = datetime_format_convertor(trade_date)
    data = w.wset('tradesuspend',
                  'startdate={start_date};enddate={end_date};field=date,wind_code,suspend_type'.format(
                          start_date = trade_date,
                          end_date = trade_date))
    return wind_symbol_back_convert(data.Data[1]).tolist()
    

def get_industry_factors(industry_wind_id,field,start_date,end_date,
                         add_industry_id = True):
    '''
    获取万得行业指数数据。
    
    Parameters
    -----------
    indusry_wind_id
        万得行业指数代码,'882100.WI'
    field
        所取字段 ['pe_ttm','pb_lf']
    start_date
        开始日期，交易日日期, 20160104，若非交易日无法取到数据
    end_date
        结束日期
    add_industry_id
        是否添加行业代码作为左后一列
    Returns
    --------
    DataFrame
        columns:wind_id,field_1,field_2,....,field_n,industry_wind_id
    
    Notes
    ------
    估值类因子
        'pe_ttm'
            市盈率TTM
        'pb_mrq'
            市净率MRQ(most recent quarter)
        'pb_lf'
            市净率LF(last file)
        'ps_ttm'
            市销率TTM
        'pcf_ocf_ttm'
            市现率TTM(经营现金流)
                    
    '''
    field_str = ','.join(field)
    data = w.wsd(industry_wind_id, field_str, 
          datetime_format_convertor(start_date),
          datetime_format_convertor(end_date), "")
    time_series = pd.Series(data.Times)
    df = pd.DataFrame(data.Data,index = field,
                      columns = time_series).T
                      
    if add_industry_id:
        df['industry_wind_id'] = industry_wind_id
    return df

def get_stock_factors(ticker,field,start_date,end_date,other = None,
                      add_ticker = True):
    '''
    获取股票因子数据。
    仅获得交易日数据。
    
    Parameters
    -----------
    ticker
        股票代码,'600340'
    field
        所取字段 ['pe_ttm','pb_lf']
    start_date
        开始日期，交易日日期, 20160104，若非交易日无法取到数据
    end_date
        结束日期
    other
        其他信息
    add_ticker
        是否添加代码作为最后一列
    Returns
    --------
    DataFrame
        index:DatetimeIndex
        columns:field_1,field_2,....,field_n,ticker
    
    Notes
    ------
    估值类因子
        'pe_ttm'
            市盈率TTM
        'pb_mrq'
            市净率MRQ(most recent quarter)
        'pb_lf'
            市净率LF(last file)
        'ps_ttm'
            市销率TTM
        'pcf_ocf_ttm'
            市现率TTM(经营现金流)                    
    '''
    field_str = ','.join(field)
    ticker_wind = wind_symbol_convert(ticker)
    if other is None:
        other = ''
    data = w.wsd(ticker_wind, field_str, 
                 datetime_format_convertor(start_date),
                 datetime_format_convertor(end_date), other)
    time_series = pd.Series(data.Times)
    df = pd.DataFrame(data.Data,index = field,
                      columns = time_series).T
    if add_ticker:
        df['ticker'] = ticker
    return df

def get_stock_factors_on_year(ticker,field,trade_date,year,add_ticker = True,
                              add_year = True):
    '''
    根据年份获取领先预测数据。
    
    Parameters
    ------------
    ticker
        '600340'
    field
        ['west_mediansales']
    trade_date
        '20170908',预测提出时间
    year
        '2018',预测年份
    add_ticker
        结果是否添加代码
    Retruns
    --------
    DataFrame
        index: datetime
        columns: field1,field2,...,ticker,year
    '''
    trade_date = datetime_format_convertor(trade_date)
    ticker_wind = wind_symbol_convert(ticker)
    field_str = ','.join(field)
    data = w.wsd(ticker_wind,field_str,trade_date,trade_date,"unit=1;year=%s;westPeriod=30"%year)
    time_series = pd.Series(data.Times)
    df = pd.DataFrame(data.Data,index = field,
                      columns = time_series).T   
    if add_ticker:
        df['ticker'] = ticker
    if add_year:
        df['year'] = year
    return df

def get_stock_factors_with_industry(ticker,field,start_date,end_date,
                                    add_ticker = True,add_industry_id = True):
    '''
    获取股票因子数据,以及对应的行业因子数据。目前支持二级行业。
    
    Returns
    --------
    DataFrame
        columns
            field_1,field_2,...,field_n,ticker,industry_field_1,...,industry_field_n,industry_wind_id
    '''
    stock_basics = get_basics(ticker)
    industry_wind_id = stock_basics['indexcode_wind'][0]
    stock_factors = get_stock_factors(ticker,field,start_date,end_date,add_ticker)
    industry_factors = get_industry_factors(industry_wind_id,field,start_date,
                                            end_date)
    industry_field = []
    for each in field:
        industry_field.append('industry_' + each)
    columns = zip(field,industry_field)
    columns = dict(columns)
    industry_factors.rename(columns = columns,inplace = True)
    df = stock_factors.join(industry_factors)
    return df

def get_stocks_factors(universe,factors,trade_date):
    '''
    获取多只股票的多个因子,仅支持单一交易日。
    
    Parameters
    -----------
    universe
        ['600340','000001']
    factors
        ['ev','pe_ttm']
    trade_date
        '20150103'

    Returns
    --------
    DataFrame
        index [ticker,...]
        columns factor1,factor2,...
    '''
    wind_universe = map(wind_symbol_convert,universe)
    wind_universe = ','.join(wind_universe)
    wind_factors = ','.join(factors)
    data = w.wss(wind_universe, wind_factors,"unit=1;tradeDate=%s"%trade_date)
    df = pd.DataFrame(data.Data,index = factors,columns = universe).T
    return df

# ------------------- Abandon ---------------------------------
def get_dividend(ticker,trade_date):
    '''
    获取股票指定时间实施的分红送股转增数据。若指定时间股票没有分红送股则返回空表。
		
    Parameters
    ----------
		ticker
			'600340'
		trade_date
			'20100101'
    Returns
    --------
		DataFrame
			index XD_date
			columns XD_date,dividend_per_share,multiplier
					(除权除息日,每股分红,分红后每股乘数)
    '''
    ticker = wind_symbol_convert(ticker)
    start_date = datetime_format_convertor(start_date)
    end_date = datetime_format_convertor(end_date)
    data = w.wsd(ticker,
          "div_exdate,div_cashaftertax,div_cashandstock", 
          start_date, end_date, "")
    df = pd.DataFrame(data.Data,index = ['XD_date','dividend_per_share',
                                        'multiplier'],columns = data.Times).T
    return df

if __name__ == '__main__':
#==============================================================================
#     data = get_stock_factors_on_year('600340',['west_mediansales'],'20170907','2018')
#==============================================================================
#==============================================================================
#     data = get_stock_factors('600340',['RSI'],'20150101','20160101','RSI_N=6')
#==============================================================================
    data = get_stocks_factors(['600340','000001'],['ev','pe_ttm'],'20170912')
