# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:03:24 2017

@author: ldh
"""

# utils.py
import datetime as dt

import numpy as np
import pandas as pd

def convert_time(date_time_ordinal):
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

convert_time = np.frompyfunc(convert_time,1,1)
