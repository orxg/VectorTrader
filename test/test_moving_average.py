# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 08:59:24 2017

@author: ldh
"""

# test_moving_average.py

from VectorTrader.api import *

import talib

def initilize(context):
    context.long_period = 30
    context.short_period = 5

def handle_bar(context,history_bars):
    universe = context.universe
    # 得到universe中股票的过去n个交易日收盘价数据
    his = history_bars.get_history(context.long_period)
    buy_list = []
    sell_list = []
    
    position = context.position
    
    for ticker in universe:
        ma_5 = talib.MA(his[ticker]['close_price'].values,context.short_period)[-1]
        ma_30 = talib.MA(his[ticker]['close_price'].values,context.long_period)[-1]
        
        if ma_5 >= ma_30 and position[ticker] == 0:
            buy_list.append(ticker)
            print context.current_date
            print ma_5
            print ma_30
        if ma_5 < ma_30 and position[ticker] > 0:
            sell_list.append(ticker)
            print context.current_date
            print ma_5
            print ma_30
            
    for ticker in sell_list:
        order(ticker,1000,-1)
    
    for ticker in buy_list:
        order(ticker,1000,1)
        
        
    
