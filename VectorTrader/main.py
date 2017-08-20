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

from data.data_proxy import DataProxy

from mod.sys_tushare_data_source.tushare_data_source import TushareDataSource
from utils.create_base_scope import create_base_scope

def all_system_go(config,strategy_path):
    '''
    主程序。启动回测/模拟/实盘。
    
    Parameters
    ----------
        config
            用户策略配置
        strategy_path
            策略路径
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
    
    ## 初始化数据
    if not env.data_source:
        env.set_data_source(TushareDataSource())
    if not env.data_proxy:
        env.set_data_proxy(DataProxy(env.data_source))
    
    print 'Loading Data...'
    env.data_proxy.load_trading_data(universe,start_date,end_date)
    print 'Loading Data Successfully'
    
    ## 初始化
    
    
    
    # 启动引擎
    Engine(env).run()

if __name__ == '__main__':
    
    config = {'base':
    {'start_date':'20100101',
     'end_date':'20150101',
     'capital':10000,
     'frequency':'1d',
     'universe':['600340']}}
        
        
    
    