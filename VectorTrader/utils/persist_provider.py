# -*- coding: utf-8 -*-
"""
Created on Mon Sep 04 08:43:46 2017

@author: ldh
"""

# persist_provider.py

import os

class DiskPersistProvider():
    '''
    提供硬盘上的持久化服务。
    '''
    def __init__(self,persist_path):
        self._persist_path = persist_path
        try:
            os.mkdir(self._persist_path)
        except:
            pass
        
    def store(self,key,value):
        assert isinstance(value,bytes), 'should be bytes'
        with open(os.path.join(self._persist_path,key),'wb') as f:
            f.write(value)
        
    def load(self,key):
        try:
            with open(os.path.join(self._persist_path,key),'rb') as f:
                return f.read()
        except:
            return None
        
    

            
    
