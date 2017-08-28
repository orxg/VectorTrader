# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:33:34 2017

@author: ldh
"""

# run_file.py

config = {'base':
    {'start_date':'20150101',
     'end_date':'20160101',
     'frequency':'1d',
     'capital':100000,
     'universe':['600340','000001']}}

from VectorTrader import run_file

strategy_path = './test/test_moving_average.py'
run_file(config,strategy_path)

