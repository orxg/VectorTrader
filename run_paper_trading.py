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
     'universe':['600340','600066']}}

from VectorTrader import run_file
strategy_path = './test/test_buy_and_hold.py'
run_file(config,'buy_and_hold',strategy_path,mode = 'p',
         persist_path = 'G:\Work_ldh\Backtest\StrategyGo\persist',
         report_path = 'G:\Work_ldh\Backtest\StrategyGo\out\paper_trading')
