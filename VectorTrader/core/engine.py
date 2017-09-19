# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:07:01 2017

@author: ldh
"""

# engine.py
import numba as nb
from ..events import EVENT,Event

PRE_BEFORE_TRADING = Event(EVENT.PRE_BEFORE_TRADING)
POST_BEFORE_TRADING = Event(EVENT.POST_BEFORE_TRADING)

PRE_BAR = Event(EVENT.PRE_BAR)
POST_BAR = Event(EVENT.POST_BAR)

PRE_AFTER_TRADING = Event(EVENT.PRE_AFTER_TRADING)
POST_AFTER_TRADING = Event(EVENT.POST_AFTER_TRADING)

PRE_SETTLEMENT = Event(EVENT.PRE_SETTLEMENT)
POST_SETTLEMENT = Event(EVENT.POST_SETTLEMENT)

class Engine():
    
    def __init__(self,env):
        '''
        引擎。执行回测、模拟、实时交易的事件驱动引擎。
        '''
        self.env = env
        
    def run(self):
        '''
        启动引擎。
        '''
        start_date = self.env.start_date
        end_date = self.env.end_date
        frequency = self.env.frequency
        
        for event in self.env.event_source.events(start_date,
                                           end_date,
                                           frequency):

            self.env.calendar_dt = event.calendar_dt
            self.env.trading_dt = event.trading_dt
            
            if event.event_type == EVENT.BEFORE_TRADING:
                self.env.event_bus.publish_event(PRE_BEFORE_TRADING)
                self.env.event_bus.publish_event(event)
                self.env.event_bus.publish_event(POST_BEFORE_TRADING)
            elif event.event_type == EVENT.BAR:
                self.env.event_bus.publish_event(PRE_BAR)
                self.env.event_bus.publish_event(event)
                self.env.event_bus.publish_event(POST_BAR)               
            elif event.event_type == EVENT.AFTER_TRADING:
                self.env.event_bus.publish_event(PRE_AFTER_TRADING)
                self.env.event_bus.publish_event(event)
                self.env.event_bus.publish_event(POST_AFTER_TRADING)  
            elif event.event_type == EVENT.SETTLEMENT:
                self.env.event_bus.publish_event(PRE_SETTLEMENT)
                self.env.event_bus.publish_event(event)
                self.env.event_bus.publish_event(POST_SETTLEMENT)  
            