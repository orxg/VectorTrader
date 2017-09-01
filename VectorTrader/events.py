# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:06:40 2017

@author: ldh
"""

# events.py
from collections import defaultdict
from enum import Enum

class Event():
    
    def __init__(self,event_type,**kwargs):
        '''
        事件。
        '''
        self.__dict__ = kwargs
        self.event_type = event_type
        
        
class EventBus():
    def __str__(self):
        event_bus_list = []
        for name,value in self.event_bus.items():
            event_bus_list.append([name,value])
        return str(event_bus_list)
            
    def __init__(self):
        self.event_bus = defaultdict(list)
        
    def add_listener(self,event_type,listener):
        self.event_bus[event_type].append(listener)
        
    def prepend_listener(self,event_type,listener):
        self.event_bus[event_type].append(listener)
        
    def publish_event(self,event):
        event_type = event.event_type
        for l in self.event_bus[event_type]:
            l(event)
            
class EVENT(Enum):
    # 系统初始化
    SYSTEM_INITILIZE = 'system_initilize'
    
    # 策略初始化
    STRATEGY_INITILIZE = 'strategy_initilize'
    
    # 交易前
    PRE_BEFORE_TRADING = 'pre_before_trading'
    BEFORE_TRADING = 'before_trading'
    POST_BEFORE_TRADING = 'post_before_trading'
    
    # Bar
    PRE_BAR = 'pre_bar'
    BAR = 'BAR'
    POST_BAR = 'post_bar'
    
    # 交易后
    PRE_AFTER_TRADING = 'pre_after_trading'
    AFTER_TRADING = 'after_trading'
    POST_AFTER_TRADING = 'post_after_trading'
    
    # 结算
    PRE_SETTLEMENT = 'pre_settlement'
    SETTLEMENT = 'settlement'
    POST_SETTLEMENT = 'post_settlement'
    
    # 订单事件
    ORDER = 'order'
    
    # 成交订单
    FILL_ORDER = 'fill_order'
    
    # 订单取消
    CANCEL_ORDER = 'cancel_order'
    
if __name__ == '__main__':
    event = Event(EVENT.AFTER_TRADING,calendar_dt = '20150101')       