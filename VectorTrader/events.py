# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:06:40 2017

@author: ldh
"""

# events.py
from collections import defaultdict
from enum import Enum

class Event():
    
    def __init__(self,event_type,**kwards):
        '''
        事件。
        '''
        self.event_type = event_type
        self.__dict__ = kwards
        
class EventBus():
    
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
    SYSTEM_INIT = 'system_init'
    
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
    
    # 订单反馈
    FILL_ORDER = 'fill_order'
    
           