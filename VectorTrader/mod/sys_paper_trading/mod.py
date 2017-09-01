# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:27:27 2017

@author: ldh
"""

# mod.py

from .realtime_event_source import PaperTradingEventSource,PaperTradingBroker
from 
class RealtimeEventSourceMod():
    def __init__(self):
        pass
    
    def start_up(self,env):
        env.set_event_source(RealtimeEventSource(env))
        
    def tear_down(self):
        pass
        

