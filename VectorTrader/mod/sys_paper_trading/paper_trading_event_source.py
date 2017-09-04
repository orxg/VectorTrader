# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:33:05 2017

@author: ldh
"""

# realtime_event_source.py

import six
import pickle
import datetime
import time 
from Queue import Queue,Empty
from threading import Thread

from VectorTrader.events import Event,EVENT
from .utils import is_holiday_today

class PaperTradingEventSource():
    def __init__(self,env):
        self.env = env
        
        self.before_trading_date = datetime.date(2000, 1, 1)
        self.after_trading_date = datetime.date(2000, 1, 1)
        self.settlement_date = datetime.date(2000, 1, 1)
        self.bar_date = datetime.date(2000, 1, 1)
        
        self._event_queue = Queue()
        self._clock_worker_thread = Thread(target = self._clock_worker)
        
    def _clock_worker(self):
        '''
        每日在指定时间生成事件。
        '''        
        while True:
            time.sleep(1)
            
            if is_holiday_today():
                time.sleep(3600)
                continue
            
            now = datetime.datetime.now()
            now_time = now.strftime('%H:%M:%S')
            now_date = now.replace(hour=0,minute=0,second=0,microsecond=0)
            if now_time >= '08:30:00' and datetime.date.today() > self.before_trading_date:
                self._event_queue.put((now_date,now,EVENT.BEFORE_TRADING))
                self.before_trading_date = datetime.date.today()
            elif now_time >= '15:10:00' and datetime.date.today() > self.bar_date:
                self._event_queue.put((now_date,now,EVENT.BAR))
                self.bar_date = datetime.date.today()                
            elif now_time >= '15:20:00' and datetime.date.today() > self.after_trading_date:
                self._event_queue.put((now_date,now,EVENT.AFTER_TRADING))
                self.after_trading_date = datetime.date.today()
            elif now_time >= '15:30:00' and datetime.date.today() > self.settlement_date:
                self._event_queue.put((now_date,now,EVENT.SETTLEMENT))
                self.settlement_date = datetime.date.today()

                
    def events(self,start_date,end_date,frequency):
        '''
        产生实时事件，启动后第二个交易日开始产生事件。目前只支持日线级别。
        '''
        running = True
        
        if frequency == '1d':
            self._clock_worker_thread.start()
            while running:
                while True:
                    try:
                        date,date_time,event_type = self._event_queue.get(timeout = 1)
                        break
                    except Empty:
                        time.sleep(1)
                        continue
                print 'NOW,THE EVENT IS %s'%event_type.name
                yield Event(event_type,calendar_dt = date,trading_dt = date_time)

# ------------------------ Abondan ------------------------------------                
    def get_state(self):
        state_data = {}
        for key,value in six.iteritems(self.__dict__):
            if key.startswith('_'):
                continue
            try:
                state_data[key] = pickle.dumps(value)
            except:
                print '{} can not be pickled'.format(key)
        return pickle.dumps(state_data)
            
    def set_state(self,state):
        state_data = pickle.loads(state)
        for key,value in six.iteritems(state_data):
            try:
                self.__dict__[key] = pickle.loads(value)
            except:
                print '{} can not be loaded'.format(key)                
            
            
            
        
        
    
        

