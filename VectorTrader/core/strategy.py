# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:08:57 2017

@author: ldh
"""

# strategy.py

from ..events import EVENT

class Strategy():
    
    def __init__(self,env,scope,context):
        '''
        用户策略抽象。
        
        Parameters
        ----------
            env
                策略所在环境。
            scope
                strategyloader返回的带有用户定义函数的namespace
            context
                用户在函数中作为传递当前环境的上下文
        '''
        self.env = env
        self._user_context = context
        
        self._initilize = scope.get('initilize',None)
        self._before_trading = scope.get('before_trading',None)
        self._handle_bar = scope.get('handle_bar',None)
        self._after_trading = scope.get('after_trading',None)
        
        if self._before_trading is not None:
            self.env.event_bus.add_listener(EVENT.BEFORE_TRADING,
                                            self.before_trading)
        if self._handle_bar is None:
            print('handle_bar is not implemented')
        self.env.event_bus.add_listener(EVENT.BAR,
                                        self.handle_bar)
        if self._after_trading is not None:
            self.env.event_bus.add_listener(EVENT.BEFORE_TRADING,
                                            self.after_trading)        
    def initilize(self):
        self._initilize(self._user_context)
            
    def before_trading(self,event):
        if self._before_trading is not None:
            self._before_trading(self._user_context)
    
    def handle_bar(self,envent):
        self._handle_bar(self._user_context)
    
    def after_trading(self,event):
        if self._after_trading is not None:
            self._after_trading(self._user_context)
        

