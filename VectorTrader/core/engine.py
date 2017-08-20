# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:07:01 2017

@author: ldh
"""

# engine.py
from ..events import EVENT


class Engine():
    
    def __init__(self,env):
        '''
        引擎。执行回测、模拟、实时交易的事件驱动引擎。
        '''
        self.env = env
        
    def run(self,start_date,end_date,frequency):
        '''
        启动引擎。
        '''
        for event in self.env.event_source(start_date,
                                           end_date,
                                           frequency):
            
        