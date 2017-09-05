# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 15:50:16 2017

@author: ldh
"""

# run_paper_trading.py

config = {'base':
    {'start_date':'20170101',
     'end_date':'20170501',
     'frequency':'1d',
     'capital':100000,
     'universe':['600381']}}

from VectorTrader import run_file
strategy_path = './test/test_buy_and_hold.py'
run_file(config,strategy_path,mode = 'p',
         persist_path = 'G:\\Work_ldh\\Backtest\\VectorTrader\\persist')
