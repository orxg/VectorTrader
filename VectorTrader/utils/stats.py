# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:56:49 2017

@author: ldh
"""

# stats.py

import numpy as np

def error_control(func,*args,**kwargs):
    def wrapper(*args,**kwargs):
        try:
            res = func(*args,**kwargs)
            return res
        except:
            return None
    return wrapper
    
@error_control
def calc_bar_return(net_value_series):
    '''
    计算每个bar的收益率。
    
    Parameters
    ----------
        net_value_series
            Series,资产净值
    '''
    net_value_series_shift = net_value_series.shift(1)    
    return_series = (net_value_series - net_value_series_shift) / net_value_series_shift
    return return_series

@error_control  
def calc_return_pnl(net_value_series):
    '''
    计算总收益率PnL.
    '''
    initial_value = net_value_series[0]
    return_pnl = (net_value_series - initial_value) / initial_value
    return return_pnl

@error_control      
def calc_total_return(net_value_series):
    last_value = net_value_series.values[-1]
    origin_value = net_value_series.values[0]
    total_return = (last_value - origin_value) / origin_value
    return total_return

@error_control
def calc_annul_return(net_value_series):
    start_date = net_value_series.index[0]
    end_date = net_value_series.index[-1]
    year_part = (end_date - start_date).days / 365.0
    total_return = calc_total_return(net_value_series)
    return total_return / year_part

@error_control
def calc_sharp_ratio(net_value_series):
    '''
    计算夏普比率。
    '''    
    bar_return = calc_bar_return(net_value_series)
    annul_return = calc_annul_return(net_value_series)
    volatility = bar_return.std()
    return annul_return / volatility

@error_control
def calc_max_drawdown(net_value_series):
    '''
    计算最大回撤相关指标。
    最大回撤、最大回撤开始结束日期；
    最长回撤期、最长回撤期开始结束日期。
    '''    
    x = net_value_series.values
    index = net_value_series.index
    max_dd_end = np.argmax(np.maximum.accumulate(x) / x)
    if max_dd_end == 0:
        max_dd_end = len(x) - 1
    max_dd_start = np.argmax(x[:max_dd_end]) if max_dd_end > 0 else 0
    
    max_dd_start_date = index[max_dd_start].to_pydatetime()
    max_dd_end_date = index[max_dd_end].to_pydatetime()
    max_dd = np.max((np.maximum.accumulate(x) - x)/ np.maximum.accumulate(x))
    
    # maxdrawdown duration
    al_cum = np.maximum.accumulate(x)
    a = np.unique(al_cum, return_counts=True)
    start_idx = np.argmax(a[1])
    m = a[0][start_idx]
    al_cum_array = np.where(al_cum == m)
    max_ddd_start_day = al_cum_array[0][0]
    max_ddd_end_day = al_cum_array[0][-1]    
    max_ddd_start_date = index[max_ddd_start_day].to_pydatetime()
    max_ddd_end_date = index[max_ddd_end_day].to_pydatetime()
    max_ddd = (max_ddd_end_date - max_ddd_start_date).days
    return max_dd,max_ddd,max_dd_start_date,\
            max_dd_end_date,max_ddd_start_date,max_ddd_end_date
    
    
if __name__ == '__main__':
    import random
    import pandas as pd
    return_list = [random.randint(-5,5)/100.0 for i in range(1000)]
    value_list = [1]
    for ret in return_list:
        value_list.append(value_list[-1] * (1 + ret))
    net_value_series = pd.Series(value_list,index = pd.date_range('20170911',periods = len(value_list)))
    print calc_total_return(net_value_series)
    print calc_annul_return(net_value_series)
    print calc_max_drawdown(net_value_series)
    print calc_sharp_ratio(net_value_series)