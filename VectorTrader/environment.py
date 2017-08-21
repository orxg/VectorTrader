# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:27:13 2017

@author: ldh
"""

# environment.py
from events import EventBus

class Environment():
    _env = None
    
    def __init__(self,config):
        Environment._env = self
        
        self.config = config # 用户定义策略基本配置
        
        self.event_bus = EventBus()
        self.event_source = None
        self.data_source = None
        self.data_proxy = None
        
        self.calendar_dt = None
        self.trading_dt = None
        
        self.start_date = None
        self.end_date = None
        self.frequency = None
        self.capital = None
        self.universe = None
        
    @classmethod
    def get_instance(cls):
        return Environment._env
    
    def set_event_source(self,event_source):
        self.event_source = event_source
        
    def set_data_source(self,data_source):
        self.data_source = data_source
    
    def set_data_proxy(self,data_proxy):
        self.data_proxy = data_proxy
    
    def set_bar_map(self,bar_map):
        self.bar_map = bar_map
        