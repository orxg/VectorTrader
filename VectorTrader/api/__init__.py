# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:23:05 2017

@author: ldh
"""

# __init__.py

from ..events import EVENT,Event
from ..environment import Environment
from ..module.orders import Order

def order(ticker,amount,direction,order_price = None):
    '''
    下单函数。在handle_bar中调用。
    '''
    env = Environment.get_instance()
    calendar_dt = env.calendar_dt
    if order_price is None:
        ## XXX : 现在用data_proxy的方式速度堪忧
        bar = env.data_proxy.get_bar(calendar_dt,ticker,
                                                     env.frequency)
        open_price = bar.open_price
        order_price = open_price
        
    order_obj = Order(env.trading_dt,ticker,amount,direction,order_price)
    order_event = Event(EVENT.ORDER,calendar_dt = env.calendar_dt,
                                trading_dt = env.trading_dt,
                                order = order_obj)
    
    env.event_bus.publish_event(order_event)
    return order_obj