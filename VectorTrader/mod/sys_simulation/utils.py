# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:58:32 2017

@author: ldh
"""

# utils.py
import datetime as dt
import pandas as pd

def daily_trading_dt(date,frequency):
    frequency = frequency[:-1] + 'T'
    frequency_int = int(frequency[:-1])
    morning_start_datetime = date.replace(hour = 9,minute = 30) + \
                                    dt.timedelta(minutes = frequency_int)
    morning_trading_dt = list(pd.date_range(start = morning_start_datetime,
                                    end = date.replace(hour=11,minute=30),
                                    freq = frequency))
    afternoon_start_datetime = date.replace(hour = 13,minute = 0) + \
                                    dt.timedelta(minutes = frequency_int)
    afternoon_trading_dt = list(pd.date_range(start = afternoon_start_datetime,
                                              end = date.replace(hour=15,minute=0),
                                              freq = frequency))
    trading_dt = morning_trading_dt + afternoon_trading_dt
    return trading_dt

if __name__ == '__main__':
    import datetime as dt
    data = daily_trading_dt(dt.datetime(2017,9,13),'20m')
    

