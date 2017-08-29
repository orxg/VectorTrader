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
from .core.history_bars import HistoryBars
from .data.data_proxy import DataProxy
from .data.data_source.mixed_data_source.mixed_data_source import MixedDataSource
from .data.data_source.tushare_data_source.tushare_data_source import TushareDataSource
from .module.bar import BarMap
from .module.account import Account
from .module.analyser import Analyser
from .module.calendar import Calendar
from .mod import ModHandler
from .utils.create_base_scope import create_base_scope
from .api.helper import get_apis

def all_system_go(config,strategy_path,mode = 'b',paper_trading_path = None):
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
        paper_trading_path
            模拟策略存储位置
    '''
    if mode == 'b':
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
        print '成功加载策略空间'
        
        ## 初始化数据源
        if not env.data_source:
            env.set_data_source(MixedDataSource())
        if not env.data_proxy:
            env.set_data_proxy(DataProxy(env.data_source,mode = mode))
        if not env.calendar:
            env.set_calendar(Calendar(env))
            
        ## 初始化MOD(事件源等)
        mod_handler = ModHandler(MOD_LIST = ['sys_simulation'])
        mod_handler.set_env(env)
        mod_handler.start_up()
        
        ## 初始化bar_map和account
        bar_map = BarMap(env.data_proxy,frequency)
        env.set_bar_map(bar_map)
        env.set_account(Account(env,capital)) # 此处account要在analyser之前
        env.set_analyser(Analyser(env))
        print '成功初始化运行环境'
        
        ## 初始化策略
        user_context = Context()
        
        history_bars = HistoryBars(env,30)
        strategy = Strategy(env,scope,user_context,history_bars)
        
        assert strategy is not None
        print '用户策略加载完成'
        
        # 启动引擎
        print '开始回测'
        env.event_bus.publish_event(Event(EVENT.SYSTEM_INITILIZE))
        env.event_bus.publish_event(Event(EVENT.STRATEGY_INITILIZE))
        Engine(env).run()
    
        # report
        env.analyser.stats()
        env.analyser.show_stats()
        
        # 关闭mod
        mod_handler.tear_down()
        
    elif mode == 'p':
        if paper_trading_path is None:
            raise ValueError('请创建模拟策略文件保存路径')
            
        env = Environment(config)
        start_date = config['base']['start_date']
        end_date = config['base']['end_date']
        capital = config['base']['capital']
        universe = config['base']['universe']
        frequency = config['base']['frequency']
        
        # 向计划任务中添加周期任务
        ## 该任务每个交易日8:10触发
        ## 包括读取用户策略，读取Account,读取用户context,创建运行环境
        ## 数据订阅
        ## 当日事件流的产生(不含initilize)
        # 初始化Account,context并保存
    
        
        
    
    