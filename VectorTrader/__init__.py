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

def run_file(config,strategy_name,strategy_path,mode = 'b',
             persist_path = None,report_path = None):
    '''
    Parameters
    ----------
        config
            用户策略配置
        strategy_name
            策略名称
        strategy_path
            策略路径
        mode
            模式 'b','p','r',支持回测'b'和模拟'p'
        persist_path
            在模拟状态下必须给出持久化路径
        report_path
            回测结果保存地址
    '''
    
    from .main import all_system_go
    return all_system_go(config,strategy_name,strategy_path,mode,persist_path,report_path)
    

