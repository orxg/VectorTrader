# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:00:35 2017

@author: ldh
"""

# __init__.py

import yaml
import os

package_path = __path__[0]
etc_path = os.path.join(package_path,'etc.yaml')

with open(etc_path,'r') as f:
    etc = yaml.load(f)

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
    if report_path is None:
        report_path = etc['report_path']
    if mode == 'p' and persist_path is None:
        persist_path = etc['persist_path']
        
    from .main import all_system_go
    return all_system_go(config,strategy_name,
                         strategy_path,mode,
                         persist_path,report_path)
    

