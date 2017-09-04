# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:33:34 2017

@author: ldh
"""

# run_strategy.py

config = {'base':
    {'start_date':'20140101',
     'end_date':'20170501',
     'frequency':'1d',
     'capital':100000,
     'universe':['600381']}}

from VectorTrader import run_file

strategy_path = './strategy/guosen/sell_too_much.py'
run_file(config,strategy_path,'b')



