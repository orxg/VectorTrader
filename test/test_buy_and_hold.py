# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:30:40 2017

@author: ldh
"""

# test_buy_and_hold.py
from VectorTrader.api import *

def initilize(context):
    context.fired = False

def before_trading(context):
    pass

def handle_bar(context,history_bars):
    if not context.fired:
        history = history_bars.get_history(10)
        print history['600340']
        order('600340',1000,1)
        context.fired = True
        
def after_trading(context):
    pass


