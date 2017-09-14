# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:33:34 2017

@author: ldh
"""

# run_strategy.py

config = {'base':
    {'start_date':'20170103',
     'end_date':'20170201',
     'frequency':'20m',
     'capital':100000,
     'universe':['600340']}}

from VectorTrader import run_file

strategy_path = './test/test_buy_and_hold.py'
run_file(config,'buy_and_hold',strategy_path,'b')



