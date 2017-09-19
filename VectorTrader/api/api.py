# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:14:33 2017

@author: ldh
"""

# api.py

__all__ = [
       'order'
       ]

from ..events import EVENT,Event
from ..environment import Environment
from ..model.orders import Order

def order(ticker,amount,direction,order_price = None):
    '''
    下单函数。在handle_bar中调用。
    '''
    env = Environment.get_instance()
    if order_price is None:       
        open_price =  env.bar_map.get_latest_bar_value(ticker,'open_price')
        order_price = open_price
            
    order_obj = Order(env.calendar_dt,env.trading_dt,
                      ticker,amount,
                      direction,order_price)
    order_event = Event(EVENT.PENDING_NEW_ORDER,
                        order = order_obj)
    
    env.event_bus.publish_event(order_event)
    return order_obj
    

# ------------------------ 3.0 支持 ------------------------------
def order_to():
    '''
    下单到指定数量。
    '''
    pass

def order_pct_to():
    '''
    下单到指定比例.
    '''
    pass