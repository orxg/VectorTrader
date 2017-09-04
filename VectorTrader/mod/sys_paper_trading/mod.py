# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:27:27 2017

@author: ldh
"""

# mod.py

from .paper_trading_event_source import PaperTradingEventSource
from .paper_trading_broker import PaperTradingBroker

class PaperTradingMod():
    def __init__(self):
        pass
    
    def start_up(self,env):
        env.set_event_source(PaperTradingEventSource(env))
        env.set_broker(PaperTradingBroker(env))
        
    def tear_down(self):
        pass
        

