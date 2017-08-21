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
        
        self.asset_value = self.cash
        
        for ticker in env.universe:
            self.position[ticker] = 0
            self.market_value[ticker] = 0
            
        self.env.event_bus.add_listener(EVENT.FILL_ORDER,self._handle_fill_order)
        self.env.event_bus.add_listener(EVENT.BAR,self._refresh) # 确保第二个接收事件
        
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
    
        self.asset_value = self.asset_value - fill_order.transaction_fee
        
    def _refresh(self,event):
        
        ## TODO : 实现bar_map功能
        bar_map = event.bar_map # bar_map包含了BAR中universe所有的close_price
        close_price_df = {}
        self.asset_value = self.cash
        for ticker,close_price in bar_map.items():
            self.market_value[ticker] = self.position[ticker] * close_price
            self.asset_value += self.position[ticker] * close_price

            
            
        
        
            
        
        
        
        