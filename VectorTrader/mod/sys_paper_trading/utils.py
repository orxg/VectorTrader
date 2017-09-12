# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:08:21 2017

@author: ldh
"""

# calendar_handler.py


def is_holiday_today():
    import datetime as dt
    today = dt.datetime.today()
    weekday =  dt.datetime.isoweekday(today)
    if weekday in range(1,6):
        return False
    else:
        return True


if __name__ == '__main__':
    a = is_holiday_today()