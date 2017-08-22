# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:00:35 2017

@author: ldh
"""

# __init__.py

def run_file(config,strategy_path,mode = 'b'):
    from .main import all_system_go
    all_system_go(config,strategy_path,mode)
    

