# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 13:35:15 2017

@author: ldh
"""

# tushare_utils.py

import tushare as ts
import pandas as pd

def get_calendar_days(start_date,end_date):
    start_date = start_date[:4] + '-' + start_date[4:6] + '-' + start_date[6:]
    end_date = end_date[:4] + '-' + end_date[4:6] + '-' + end_date[6:]
    data = ts.get_k_data('000001',start_date,end_date,index = True)
    data = pd.to_datetime(data['date'])
    return data

if __name__ == '__main__':
    data = get_calendar_days('20150101','20160101')

