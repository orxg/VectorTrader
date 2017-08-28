# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:56:49 2017

@author: ldh
"""

# stats.py

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
    

def calc_return_pnl(net_value_series):
    '''
    计算总收益率PnL.
    '''
    initial_value = net_value_series[0]
    return_pnl = (net_value_series - initial_value) / initial_value
    return return_pnl
    