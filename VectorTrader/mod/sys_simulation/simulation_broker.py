# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:23:37 2017

@author: FSB
"""

# simulation_broker.py

from VectorTrader.events import EVENT,Event
from VectorTrader.module.orders import FillOrder

class SimulationBroker():
    def __init__(self,env):
        self.env = env
        
        event_bus = env.event_bus
        event_bus.add_listener(EVENT.ORDER,self._match_order)
        
    def _match_order(self,event):
        order = event.order
        
        calendar_dt = event.calendar_dt
        trading_dt = event.trading_dt
        ticker = order.ticker
        amount = order.amount
        direction = order.direction
        order_price = order.order_price
        
        # 暂时不加检查地让其成交
        ##TODO :根据current_bar_map进行撮合
        match_amount = amount
        match_price = order_price
        ##TODO : 细化交易费用
        transaction_fee = 5 # 交易费用
        
        fill_order_obj = FillOrder(trading_dt,ticker,match_amount,
                                   direction,transaction_fee,
                                   match_price)
        fill_event = Event(EVENT.FILL_ORDER,calendar_dt = calendar_dt,
                           trading_dt = trading_dt,fill_order = fill_order_obj)
        
        self.env.event_bus.publish_event(fill_event)
        
        
    