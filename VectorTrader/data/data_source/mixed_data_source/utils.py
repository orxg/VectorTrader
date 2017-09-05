# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:03:24 2017

@author: ldh
"""

# utils.py
import datetime as dt

import numpy as np
import pandas as pd


## Wind专有
def wind_symbol_convert(symbol):
    if symbol[0] == '6':
        wind_symbol = symbol + '.SH'
    else:
        wind_symbol = symbol + '.SZ'
    return wind_symbol

def wind_symbol_back_convert(symbol):
    return symbol[:6]

wind_symbol_back_convert = np.frompyfunc(wind_symbol_back_convert,1,1)

## MATLAB专有
def matlab_time_convert(date_time_ordinal):
    '''
    转换时间(从公元前1年1月1日),支持到分钟级。
    已经与matlab一致。
    下面的数据可以在matlab上测试。完美(比matlab.datestr精确1s)。
    
    
    0      736819.593056    600340  36.4200 2017-05-04 14:14:00
    1      736819.593750    600340  36.3999 2017-05-04 14:15:00
    2      736819.594444    600340  36.3500 2017-05-04 14:16:00
    3      736819.595139    600340  36.3100 2017-05-04 14:17:00
    4      736819.595833    600340  36.2299 2017-05-04 14:18:00
    5      736819.596528    600340  36.1899 2017-05-04 14:19:00
    '''
    
    int_part = int(date_time_ordinal)
    float_part = date_time_ordinal - int_part
    seconds = int(float_part * 24 * 60 * 60) + 1
    
    date_part = dt.datetime.fromordinal(int_part - 366 )
    time_part = dt.timedelta(seconds = seconds) 
    date_time = date_part + time_part
    time_adjustor = pd.offsets.DateOffset(second = 0,microsecond = 0)
    date_time = date_time + time_adjustor
    return date_time

matlab_time_convert = np.frompyfunc(matlab_time_convert,1,1)

def datetime_format_convertor(datetime_str):
    '''
    将20150101格式转换成2015-01-01格式。
    '''
    date_time = datetime_str[:4] + '-' + datetime_str[4:6] + '-' + datetime_str[6:]
    return date_time

## 其他
def convert_to_datetime(time_stamp):
    '''
    把pandas.Timestamp对象转换成datetime.
    '''
    return time_stamp.to_pydatetime()

convert_to_datetime = np.frompyfunc(convert_to_datetime,1,1)

# 用于将从guosen数据库中读取的数据Decimal类型转换成float
convert_to_float = np.frompyfunc(np.float,1,1)
    