# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:40:35 2017

@author: ldh
"""

# main.py
from .events import EVENT,Event
from .environment import Environment
from .core.engine import Engine
from .core.strategy import Strategy
from .core.strategy_loader import StrategyLoader
from .core.context import Context
from .data.data_proxy import DataProxy
from .data.data_source.tushare_data_source.tushare_data_source import TushareDataSource
from .module.bar import BarMap
from .module.account import Account
from .module.analyser import Analyser
from .mod import ModHandler
from .utils.create_base_scope import create_base_scope
from .api.helper import get_apis

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
    
    start_date = config['base']['start_date']
    end_date = config['base']['end_date']
    capital = config['base']['capital']
    universe = config['base']['universe']
    frequency = config['base']['frequency']
    
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
    apis = get_apis()
    scope.update(apis)
    scope = strategy_loader.load(scope)
    print 'Successfully loaded the user\'s stategy scope'
    
    ## 初始化数据源
    if not env.data_source:
        env.set_data_source(TushareDataSource())
    if not env.data_proxy:
        env.set_data_proxy(DataProxy(env.data_source,mode = mode))
        
    ## 初始化事件源
    mod_handler = ModHandler()
    mod_handler.set_env(env)
    mod_handler.start_up()
       
    bar_map = BarMap(env.data_proxy,frequency)
    env.set_bar_map(bar_map)
    env.set_account(Account(env,capital))
    env.set_analyser(Analyser(env))
    
    print 'Successfully initilized running environment'
    ## 初始化策略
    user_context = Context()
    strategy = Strategy(env,scope,user_context)
    assert strategy is not None
    print 'Strategy loaded complete'
    
    # 启动引擎
    print 'The system is going to run'
    env.event_bus.publish_event(Event(EVENT.SYSTEM_INITILIZE))
    env.event_bus.publish_event(Event(EVENT.STRATEGY_INITILIZE))
    Engine(env).run()

    env.analyser.plot_pnl()
    
    mod_handler.tear_down()
    
        
        
    
    