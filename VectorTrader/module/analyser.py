# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:52:45 2017

@author: LDH
"""

# analyser.py
import pandas as pd

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
        calendar_dt = self.env.calendar_dt
        trading_dt = self.env.trading_dt
        account = self.env.account
        self.portfolio_net_value.append([calendar_dt,trading_dt,account.total_asset_value])
        self.position_record.append([calendar_dt,trading_dt,account.position])
        
        
    def plot_pnl(self):
        pnl_df = pd.DataFrame(self.portfolio_net_value,columns = ['calendar_dt',
                                                                  'trading_dt',
                                                                  'total_asset_value'])
        pnl_df = pnl_df[['calendar_dt','total_asset_value']]
        pnl_df = pnl_df.set_index('calendar_dt')
        pnl_df.plot()
    
    