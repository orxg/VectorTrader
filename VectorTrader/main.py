# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:40:35 2017

@author: ldh
"""

# main.py
import datetime
import numba as nb

from .events import EVENT,Event
from .environment import Environment
from .core.engine import Engine
from .core.strategy import Strategy
from .core.strategy_loader import StrategyLoader
from .core.dynamic_universe import DynamicUniverse
from .core.context import Context
from .data.data_proxy import DataProxy
from .data.data_source.mixed_data_source.mixed_data_source import MixedDataSource
from .model.account import Account
from .model.analyser import Analyser
from .model.calendar import Calendar
from .model.bar import BarMap
from .mod import ModHandler
from .utils.parse_config import Config
from .utils.create_base_scope import create_base_scope
from .utils.persist_provider import DiskPersistProvider
from .utils.persist_helper import PersistHelper
from .api.helper import get_apis

def all_system_go(config,strategy_name,strategy_path,
                  mode = 'b',persist_path = None,
                  report_path = None):
    '''
    主程序。启动回测/模拟/实盘。
    
    Parameters
    ----------
        config
            用户策略配置
        strategy_name
            策略名称
        strategy_path
            策略路径
        mode
            模式 'b','p','r'
        persist_path
            在模拟状态下必须给出持久化路径
        report_path
            回测结果保存地址
    '''
    config = Config(config)
    env = Environment(config)
    if mode == 'b':
        MOD_LIST = ['sys_simulation']
        start_date = config.start_date
        end_date = config.end_date
        capital = config.capital
        universe = config.universe
        frequency = config.frequency
        position_base = config.position_base
        cost_base = config.cost_base
    elif mode == 'p':
        MOD_LIST = ['sys_email_sender','sys_paper_trading']    
        start_date = datetime.datetime.today().strftime('%Y%m%d')
        end_date = start_date
        capital = config.capital
        universe = config.universe
        frequency = config.frequency       
        position_base = config.position_base
        cost_base = config.cost_base
        
    # 初始化环境
    ## 环境基本参数
    env.start_date = start_date
    env.end_date = end_date
    env.capital = capital
    env.frequency = frequency
    env.universe = universe
    env.mode = mode
    
    ## 读取用户策略空间
    scope = create_base_scope()
    strategy_loader = StrategyLoader(strategy_path)
    apis = get_apis()
    scope.update(apis)
    scope = strategy_loader.load(scope)
    print 'Loading strategy scope successfully'.upper()
    ## 初始化数据源,动态股票池
    if not env.data_source:
        env.set_data_source(MixedDataSource())  
    if not env.calendar:
        env.set_calendar(Calendar(env))
    if not env.data_proxy:
        env.set_data_proxy(DataProxy(env.data_source,mode = mode))
        
       
    ## 初始化MOD(事件源等)
    mod_handler = ModHandler(MOD_LIST)
    mod_handler.set_env(env)
    mod_handler.start_up()
    
    ## 初始化account,dynamic_universe
    dynamic_universe = DynamicUniverse()
    env.set_dynamic_universe(dynamic_universe) # 此处dynamic_universe要在account之前以保证监听函数靠前
    account = Account(env,capital)
    if position_base is not None and cost_base is not None:
        account.set_position(position_base,cost_base)
    env.set_account(account) # 此处account要在analyser之前
    env.set_analyser(Analyser(env,strategy_name,report_path))
    print 'Initilizing running environment successfully'.upper()
    
    ## 初始化策略
    user_context = Context()
    env.set_context(user_context)
    bar_map = BarMap(env)
    env.set_bar_map(bar_map)
    strategy = Strategy(env,scope,user_context,bar_map)
    assert strategy is not None
    strategy.initilize()
    print 'Loading strategy successfully'.upper()
    
    ## 进行持久化注册
    if mode == 'p':
        persist_provider = DiskPersistProvider(persist_path)
        persist_helper = PersistHelper(persist_provider,env.event_bus,mode)
        persist_helper.rigister('user_context',user_context)
        persist_helper.rigister('account',env.account)
        persist_helper.rigister('analyser',env.analyser)
    
        ### 从硬盘中恢复到最新的状态
        persist_helper.restore()
        print 'Restore successfully'.upper()
        
    # 启动引擎
    print 'Start running...'.upper()
    env.event_bus.publish_event(Event(EVENT.SYSTEM_INITILIZE))
    Engine(env).run()

    # report
    env.analyser.stats()
    env.analyser.show_stats()
    # 关闭mod
    mod_handler.tear_down()
    
    return env.analyser.report
        
        
    
    