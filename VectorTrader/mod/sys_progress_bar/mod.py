# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:39:37 2017

@author: ldh
该模块仅能在cmd模式下正常运行。
"""

# mod.py
from VectorTrader.environment import Environment
from VectorTrader.interface import AbstractMod
from VectorTrader.events import EVENT
import click

class ProgressBarMod(AbstractMod):
    def __init__(self):
        self._progress_bar = None
        self._trading_length = 0
        self._env = None
        
    def start_up(self,env):
        self._env = env
        env.event_bus.add_listener(EVENT.SYSTEM_INITILIZE,
                                   self._init_progress_bar)
        env.event_bus.add_listener(EVENT.POST_AFTER_TRADING,
                                   self._update_progress_bar)
    
    def _init_progress_bar(self,event):
        self._trading_length = len(self._env.data_proxy.get_calendar_days(self._env.start_date,
                                                                          self._env.end_date))
        self._progress_bar = click.progressbar(length = self._trading_length,
                                               show_eta = False)

    def _update_progress_bar(self,event):
        self._progress_bar.update(1)
        
    def tear_down(self):
        self._progress_bar.render_finish()
    
    
    
        
    
    

