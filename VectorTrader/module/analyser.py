# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:52:45 2017

@author: LDH
"""

# analyser.py
from ..events import EVENT

class Analyser():

    def __init__(self,env):
        self.env = env
        
        self.portfolio_net_value = []
        self.position_record = []
        self.order_record = []
        self.fill_order_record = []
        
        self.env.event_bus.add_listener(EVENT.POST_BAR,self._record_account)
        
    def _record_account(self,event):
        calendar_dt = event.calendar_dt
        trading_dt = event.trading_dt
        account = event.account
        self.portfolio_net_value.append([calendar_dt,trading_dt,account.asset_value])
        self.position_record.append([calendar_dt,trading_dt,account.position])
        
        
    def plot_pnl(self):
        pass
    
    