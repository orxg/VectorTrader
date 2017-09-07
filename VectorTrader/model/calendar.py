# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:31:45 2017

@author: ldh
"""

# calendar.py
import pandas as pd
import datetime as dt

class Calendar():
    def __init__(self,env):
        self._env = env
        self.data_source = self._env.data_source
        self.start_date = self._env.start_date
        self.end_date = dt.datetime.today().strftime('%Y%m%d')
        self._calendar = pd.Series(self.data_source.get_calendar_days('19910101',self.end_date))

    def adjust_date(self,origin_date,step):
        '''
        根据交易日历调整日期，得到调整后的日期。
        step为正表示向未来前进；step为负数表示向过去前进。
        '''
        try:
            idx = self._calendar.searchsorted(origin_date)[0]
            adjust_idx = idx + step
            adjusted_date = self._calendar[adjust_idx]
            return adjusted_date
        except Exception as e:
            print e
            print 'can\'t get adjusted date!'
            raise
            

