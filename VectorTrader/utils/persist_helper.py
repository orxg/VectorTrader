# -*- coding: utf-8 -*-
"""
Created on Mon Sep 04 08:46:56 2017

@author: ldh
"""

# persist_helper.py

import hashlib
from ..events import EVENT

class PersistHelper():
    '''
    对注册的对象提供持久化服务。
    '''
    def __init__(self,persist_provider,event_bus,persist_mode):
        self._objects = {}
        self._last_state = {}
        self._persist_provider = persist_provider
        if persist_mode == 'p':
            event_bus.add_listener(EVENT.POST_AFTER_TRADING,self.persist)
            event_bus.add_listener(EVENT.POST_SETTLEMENT,self.persist)
            
            
    def rigister(self,key,obj):
        '''
        注册对象。
        '''
        if key in self._objects:
            raise RuntimeError('duplicated persist key found:{}'.format(key))
        self._objects[key] = obj   
        
    def persist(self,event):
        '''
        将注册的对象状态保存在硬盘上。
        '''
        for key,obj in self._objects.items():
            state = obj.get_state()
            if not state:
                continue
            md5 = hashlib.md5(state).hexdigest()
            if self._last_state.get(key) == md5:
                continue
            self._persist_provider.store(key,state)
            self._last_state[key] = md5
                
    def restore(self):
        '''
        将注册的对象恢复到硬盘上记录的状态。
        对象需要实现set_state方法,该方法通过传递state进行对象恢复。
        '''
        for key,obj in self._objects.items():
            state = self._persist_provider.load(key)
            if not state:
                print 'restore state failed on {}'.format(key)
                continue
            obj.set_state(state)
    
    
        
        

