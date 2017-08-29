# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:08:21 2017

@author: ldh
"""

# calendar_handler.py

import datetime

def is_holiday_today():
    from VectorTrader.environment import Environment
    today = datetime.datetime.today()
    env = Environment.get_instance()
    data_proxy = env.data_poxy
    return data_proxy.is_trade_date(today)

