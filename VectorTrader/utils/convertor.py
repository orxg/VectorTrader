# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:44:30 2017

@author: ldh
"""

# convertor.py
import pandas as pd
from ..module.bar import Bar

def dataframe_to_bars(df,ticker,frequency):
    '''
    将DataFrame转换成bars.
    Parameters
    ------------
        df
            DataFrame
                index:date_time
                columns:open_price,high_price,low_price,close_price,volume
        ticker
            股票代码
        frequency
            频率
    '''
    bars_list = []
    for (date_time,series) in df.iterrows():
        bar = Bar(date_time,ticker,frequency)
        bar.close_price = series['close_price']
        bar.open_price = series['open_price']
        bar.high_price = series['high_price']
        bar.low_price = series['low_price']
        bar.volume = series['volume']
        bars_list.append(bar)
    return bars_list
    
def bars_to_dataframe(bars):
    '''
    将bars转换成DataFrame
    '''
    date_time = []
    data = []
    for bar in bars:
        date_time.append(bar.date_time)
        data.append([bar.open_price,bar.high_price,bar.low_price,bar.close_price,bar.volume])
     
    columns = ['open_price','high_price','low_price','close_price','volume']
    df = pd.DataFrame(data,index = date_time,columns = columns)
    return df
    
def list_to_generator(the_list):
        for each in the_list:
            yield each
