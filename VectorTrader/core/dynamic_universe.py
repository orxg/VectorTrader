# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:04:01 2017

@author: ldh
"""

# dynamic_universe.py
from ..events import EVENT

class DynamicUniverse():
    
    def __init__(self,env):
        self.env = env
        self.data_proxy = self.env.data_proxy
        self.user_universe = env.universe
        self.dynamic_universe = []
        
        self.env.event_bus.add_listener(EVENT.PRE_BEFORE_TRADING,self._refresh_pre_before_trading)
        
    def _refresh_pre_before_trading(self,event):
        self.dynamic_universe = []
        for ticker in self.user_universe:
            if self.data_proxy.if_current_date_trade(self.env.calendar_dt):
                self.dynamic_universe.append(ticker)
        

