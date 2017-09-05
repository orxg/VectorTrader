# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 13:35:15 2017

@author: ldh
"""

# tushare_utils.py

import tushare as ts
import pandas as pd

def get_symbols(symbol):
    '''
    获取**当前**全A、指定板块、指数、ST的成分股代码。
    Parameters
    -----------
        symbol 获取类型
    Returns
    ----------
        list [ticker,...]
    Notes
    ---------
    'A' 
        全A股
    'st' 
        st股票
    'hs300' 
        沪深300成分股
    'cyb' 
        创业板成分股
    'sz50' 
        上证50成分股
    'A-st' 
        剔除st股票后的全A股
    
    '''
    if symbol == 'A':
        return ts.get_stock_basics().index.values.tolist()
    if symbol == 'st':
        return ts.get_st_classified()['code'].values.tolist()
    if symbol == 'hs300':
        return ts.get_hs300s()['code'].values.tolist()
    if symbol == 'cyb':
        return ts.get_gem_classified()['code'].values.tolist()
    if symbol == 'sz50':
        return ts.get_sz50s()['code'].values.tolist()
    if symbol == 'A-st':
        A = set(ts.get_stock_basics().index.values.tolist())
        ST = set(ts.get_st_classified()['code'].values.tolist())
        for st in ST:
            A.discard(st)
        return list(A)
    
def get_calendar_days(start_date,end_date):
    start_date = start_date[:4] + '-' + start_date[4:6] + '-' + start_date[6:]
    end_date = end_date[:4] + '-' + end_date[4:6] + '-' + end_date[6:]
    data = ts.get_k_data('000001',start_date,end_date,index = True)
    data = pd.to_datetime(data['date'])
    return data

if __name__ == '__main__':
    data = get_symbols('sz50')

