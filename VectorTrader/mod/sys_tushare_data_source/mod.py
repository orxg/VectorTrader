# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:31:20 2017

@author: ldh
"""

# mod.py

from .tushare_data_source import TushareDataSource

class TushareDataSourceMOD():
    def __init__(self):
        pass
    
    def start_up(self,env):
        env.set_data_source(TushareDataSource())

