# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:04:01 2017

@author: ldh
"""

# dynamic_universe.py

import json
from ..events import EVENT
from ..environment import Environment

class DynamicUniverse():
    
    def __init__(self):
        env = Environment.get_instance()
        self.user_universe = env.universe
        self.dynamic_universe = []        
        env.event_bus.add_listener(EVENT.PRE_BEFORE_TRADING,self._refresh_pre_before_trading)
        
    def _refresh_pre_before_trading(self,event):
        self.dynamic_universe = []
        env = Environment.get_instance()
        for ticker in self.user_universe:
            if env.data_proxy.is_date_trade(ticker,env.calendar_dt):
                self.dynamic_universe.append(ticker)

# ------------------------------- Abandon -------------------------------                
    def get_state(self):
        return json.dumps(self.dynamic_universe).encode('utf8')
            
    def set_state(self,state):
        dynamic_universe = json.loads(state.decode('utf8'))
        self.dynamic_universe = dynamic_universe
        

