# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:12:51 2017

@author: ldh

"""

# __init__.py

from importlib import import_module

MOD_LIST = ['sys_tushare_data_source','sys_simulation']

class ModHandler():
    def __init__(self):
        self._mod_list = []
        # self._mod_path = 'G:/Work_ldh/Backtest/VectorTrader/VectorTrader/mod/'
        self.mod_dict = {}
        
    def set_env(self,environment):
        self.env = environment
        
        for mod_name in MOD_LIST:           
            self._mod_list.append(mod_name)
            
        for mod_name in self._mod_list:
            module = import_module(mod_name)
            mod = module.load_mod()
            self.mod_dict[mod_name] = mod
            
    def start_up(self):
        for mod_name in self.mod_dict:
            self.mod_dict[mod_name].start_up(self.env)
            
if __name__ == '__main__':
    mod_handler = ModHandler()