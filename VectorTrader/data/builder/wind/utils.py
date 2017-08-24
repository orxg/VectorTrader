# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:24:02 2017

@author: FSB
"""

# utils.py

import numpy as np

def symbol_convertor_wind(symbol):
    if symbol[0] == '6':
        wind_symbol = symbol + '.SH'
    else:
        wind_symbol = symbol + '.SZ'
    return wind_symbol

def convert_to_datetime(time_stamp):
    '''
    把pandas.Timestamp对象转换成datetime.
    '''
    return time_stamp.to_pydatetime()

convert_to_datetime = np.frompyfunc(convert_to_datetime,1,1)

if __name__ == '__main__':
    import pandas as pd
    ts1 = pd.Timestamp('20150101')
    ts2 = pd.Timestamp('20150202')
    ts_c = convert_to_datetime([ts1,ts2])