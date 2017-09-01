# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:25:40 2017

@author: ldh
"""

# simulation_event_source.py
from VectorTrader.events import Event,EVENT

class SimulationEventSource():
    
    def __init__(self,env):
        self.env = env
    
    def events(self,start_date,end_date,frequency):
        '''
        事件流。
        计划支持:1m,2m,3m,5m,10m,20m,30m,60m,120m
        '''
        calendar_days = self.env.data_proxy.get_calendar_days(start_date,
                                                         end_date)
        if frequency[-1] == 'd':
            for day in calendar_days:
                date = day.to_pydatetime()
                dt_before_trading = date.replace(hour=0,minute=0)
                dt_bar = date.replace(hour=15,minute=0)
                dt_after_trading = date.replace(hour=15,minute=30)
                dt_settlement = date.replace(hour=19,minute=0)
                
                yield Event(EVENT.BEFORE_TRADING,
                            calendar_dt = date,
                            trading_dt = dt_before_trading)
                yield Event(EVENT.BAR,
                            calendar_dt = date,
                            trading_dt = dt_bar)
                yield Event(EVENT.AFTER_TRADING,
                            calendar_dt = date,
                            trading_dt = dt_after_trading)
                yield Event(EVENT.SETTLEMENT,
                            calendar_dt = date,
                            trading_dt = dt_settlement)
                
        ## TODO : 分钟线
        elif frequency[-1] == 'm':
            for day in calendar_days:
                date = day.to_pydatetime()
                dt_before_trading = date.replace(hour=0,minute=0)
                pass
        
            
    