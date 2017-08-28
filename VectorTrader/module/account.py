# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:11:54 2017

@author: ldh
"""

# account.py
from ..events import EVENT

class Account():
    
    def __init__(self,env,cash):
        
        self.env = env
        
        self.cash = cash
        self.position = {}
        self.market_value = {}
        
        self.total_asset_value = self.cash
        
        for ticker in env.universe:
            self.position[ticker] = 0
            self.market_value[ticker] = 0
            
        self.env.event_bus.add_listener(EVENT.FILL_ORDER,self._handle_fill_order)
        self.env.event_bus.add_listener(EVENT.POST_BAR,self._refresh) # 确保第一个接收事件
        
    def _handle_fill_order(self,event):
        '''
        监听Broker返回的FillOrder事件。
        '''
        fill_order = event.fill_order

        self.cash += - fill_order.direction * fill_order.amount * fill_order.match_price - \
            fill_order.transaction_fee
        self.position[fill_order.ticker] += fill_order.direction * \
            fill_order.amount
        self.market_value[fill_order.ticker] += fill_order.direction * \
            fill_order.amount * fill_order.match_price
    
        self.total_asset_value = self.total_asset_value - fill_order.transaction_fee
        
    def _refresh(self,event):

        bar_map = self.env.bar_map 
        universe = self.env.universe
        calendar_dt = self.env.calendar_dt
        bar_map.update_dt(calendar_dt)
        self.total_asset_value = self.cash
        for ticker in universe:
            close_price = bar_map[ticker].close_price
            self.market_value[ticker] = self.position[ticker] * close_price
            self.total_asset_value += self.position[ticker] * close_price

            
            
        
        
            
        
        
        
        