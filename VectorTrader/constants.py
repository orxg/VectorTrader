# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 09:02:46 2017

@author: ldh
"""

# constants.py

from enum import Enum

class MODE(Enum):
    BACKTEST = 'BACKTEST'
    PAPER_TRADING = 'PAPER_TRADING'
    
class ORDER_TYPE(Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    
class ORDER_STATUS(Enum):
    NEW = 'NEW'
    FILL = 'FILL'

class SIDE(Enum):
    BUY = 'BUY'
    SELL = 'SELL'