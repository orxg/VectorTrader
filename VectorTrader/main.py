# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:40:35 2017

@author: ldh

config的形式如下:
config = {'base':
    {'start_date':'20100101',
     'end_date':'20150101',
     'capital':10000,
     'frequency':'1d',
     'universe':['600340']}}
"""

    
# main.py
from environment import Environment
from core.engine import Engine
from core.strategy import Strategy
from core.strategy_loader import StrategyLoader
from core.context import Context

from data.data_proxy import DataProxy

from module.bar import BarMap

from mod import ModHandler
from utils.create_base_scope import create_base_scope

def all_system_go(config,strategy_path,mode = 'b'):
    '''
    主程序。启动回测/模拟/实盘。
    
    Parameters
    ----------
        config
            用户策略配置
        strategy_path
            策略路径
        mode
            模式 'b','p','r'
    '''
    env = Environment(config)
    
    start_date = config.base.start_date
    end_date = config.base.end_date
    capital = config.base.capital
    universe = config.base.universe
    frequency = config.base.frequency
    
    # 初始化环境
    ## 环境基本参数
    env.start_date = start_date
    env.end_date = end_date
    env.capital = capital
    env.frequency = frequency
    env.universe = universe
    
    ## 读取用户策略空间
    scope = create_base_scope()
    strategy_loader = StrategyLoader(strategy_path)
    scope = strategy_loader.load(scope)
    
    ## 初始化数据源、事件源，确定功能类型
    mod_handler = ModHandler()
    mod_handler.set_env(env)
    mod_handler.start_up()
    
    if not env.data_proxy:
        env.set_data_proxy(DataProxy(env.data_source,mode = mode))
    
    bar_map = BarMap(env.data_proxy,frequency)
    env.set_bar_map(bar_map)
    
    ## 初始化策略
    user_context = Context()
    strategy = Strategy(env,scope,user_context)
    
    # 启动引擎
    Engine(env).run()

if __name__ == '__main__':
    
    config = {'base':
    {'start_date':'20100101',
     'end_date':'20150101',
     'capital':10000,
     'frequency':'1d',
     'universe':['600340']}}
        
        
    
    