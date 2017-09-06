# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 15:46:16 2017

@author: ldh
"""

# mod.py

from VectorTrader.interface import AbstractMod
from VectorTrader.events import EVENT

from .email_sender import send_email

class EmailSenderMod(AbstractMod):
    def __init__(self):
        self.from_addr = 'vectortrader@163.com'
        self.password = 'vectortrader2017'
        self.to_addr = '343091787@qq.com'
        self.privilege_password = 'vectortrader123'
        self.smtp_server = 'smtp.163.com'
    
    def start_up(self,env):
        self.env = env
        event_bus = env.envent_bus
        event_bus.add_listener(EVENT.POST_BEFORE_TRADING,self._send_email_post_before_trading)
    
    def tear_down(self):
        pass
    
    def _send_email_post_before_trading(self,event):
        '''
        在before_trading运行后发送指定信息的email到指定邮箱。
        '''
        content = self.env.context.signal_post_before_trading
        if content is None:
            return
        else:
            send_email(self.from_addr,self.privilege_password,self.to_addr,
                       self.smtp_server,content)
        
    



