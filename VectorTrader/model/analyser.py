# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:52:45 2017

@author: LDH
"""

# analyser.py
import pickle
from ..events import EVENT


class Analyser():

    def __init__(self,env,name = None,path = None):
        self.env = env
        self.name = name
        self.path = path
        
        self.portfolio_value = []
        self.daily_portfolio_value = []
        self.position = []
        self.daily_position = []
                
        self.history_orders = []
        self.history_fill_orders = []
        self.history_rejected_orders = []
        self.history_kill_orders = []
        
        self.env.event_bus.add_listener(EVENT.POST_BAR,self._record_post_bar)
        self.env.event_bus.add_listener(EVENT.PENDING_NEW_ORDER_PASS,self._collect_new_order)
        self.env.event_bus.add_listener(EVENT.REJECT_ORDER,self._collect_rejected_order)
        self.env.event_bus.add_listener(EVENT.TRADE,self._collect_fill_order)
        self.env.event_bus.add_listener(EVENT.KILL_ORDER_PASS,self._collect_kill_order)
        self.env.event_bus.add_listener(EVENT.SETTLEMENT,self._record_daily_settlement)
        
    def get_state(self):
        return pickle.dumps({
                'portfolio_value':self.portfolio_value,
                'daily_portfolio_value':self.daily_portfolio_value,
                'position':self.position,
                'daily_position':self.daily_position,
                'history_orders':self.history_orders,
                'history_fill_orders':self.history_fill_orders,
                'history_rejected_orders':self.history_rejected_orders,
                'history_kill_orders':self.history_kill_orders
                 })
        
    def set_state(self,state):
        state = pickle.loads(state)
        self.portfolio_value = state['portfolio_value']
        self.daily_portfolio_value = state['daily_portfolio_value']
        self.position = state['position']
        self.daily_position = state['daily_position']
        self.history_orders = state['history_orders']
        self.history_fill_orders = state['history_fill_orders']
        self.history_rejected_orders = state['history_rejected_orders']
        self.history_kill_orders = state['history_kill_orders']
    
    def _record_post_bar(self,event):
        calendar_dt = self.env.calendar_dt
        trading_dt = self.env.trading_dt
        account = self.env.account
        self.portfolio_value.append([calendar_dt,trading_dt,
                                     account.total_account_value])
        self.position.append([calendar_dt,trading_dt,
                              account.position.position])
    
    def _record_daily_settlement(self,event):
        calendar_dt = self.env.calendar_dt
        trading_dt = self.env.trading_dt
        account = self.env.account
        self.daily_portfolio_value.append([calendar_dt,trading_dt,
                                     account.total_account_value])
        self.daily_position.append([calendar_dt,trading_dt,
                              account.position.position])
            
    def _collect_new_order(self,event):
        new_order = event.order
        order_state = new_order.get_state()
        self.history_orders.append(order_state)
    
    def _collect_rejected_order(self,event):
        rejected_order = event.order
        reason = event.reason
        order_state = rejected_order.get_state()
        order_state['reject_reason'] = reason
        self.history_rejected_orders.append(order_state)
    
    def _collect_fill_order(self,event):
        fill_order = event.order
        order_state = fill_order.get_state()
        self.history_fill_orders.append(order_state)
    
    def _collect_kill_order(self,event):
        kill_order = event.order
        order_state = kill_order.get_state()
        self.history_kill_orders.append(order_state)
        
    def report(self):
        '''
        produce the running result and save it into the target file.
        '''
        import os
        file_name = os.path.join(self.path,self.name)
        state = pickle.loads(self.get_state())
        with open(file_name + '.pkl','w') as f:
            pickle.dump(state,f)
        return state

       
    
    
    