# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:00:35 2017

@author: ldh
"""

# __init__.py

import sys
import os

cwd = os.getcwd() 
mod_directory = cwd + '\\VectorTrader\\mod\\'
sys.path.append(cwd)
sys.path.append(mod_directory)

def run_file(config,strategy_path,mode = 'b'):
    from .main import all_system_go
    all_system_go(config,strategy_path,mode)
    

