# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:04:37 2017

@author: ldh
"""

# sell_too_much.py

from VectorTrader.api import *

def initilize(context):
    context.up_incline_distance = 0.1
    context.subtle_up_incline_distance = 0.02
    context.gap_distance = 0.03

def handle_bar(context,history_bars):
    universe = context.universe
    stock = universe[0]
    hist = history_bars.get_history(30)[stock]
    
    # 判断是否有gap
    kline_21 = hist.iloc[21,:]
    kline_22 = hist.iloc[22,:]
    max_price_22 = kline_22.max()
    min_price_21 = kline_21.min()
    if (min_price_21 - max_price_22) / max_price_22 < context.gap_distance:
        return
    
    # 在已经有gap的情况下判断是否有两个incline
    kline_20 = hist.iloc[20,:]
    kline_0 = hist.iloc[0,:]
    kline_27 = hist.iloc[27,:]
    kline_23 = hist.iloc[23,:]
    close_price_20 = kline_20['close_price']
    close_price_0 = kline_0['close_price']
    close_price_27 = kline_27['close_price']
    close_price_23 = kline_23['close_price']
    
    if (close_price_20 - close_price_0) / close_price_0 <= context.up_incline_distance:
        return
    
    if (close_price_27 - close_price_23) / close_price_23 <= context.subtle_up_incline_distance:
        return
    
    order(stock,2000,1)



