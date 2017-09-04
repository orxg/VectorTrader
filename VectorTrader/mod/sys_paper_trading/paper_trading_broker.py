# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:17:24 2017

@author: ldh
"""

# paper_trading_broker.py

from VectorTrader.events import EVENT,Event
from VectorTrader.module.orders import FillOrder

class PaperTradingBroker():
    def __init__(self,env):
        self.env = env
        event_bus = env.event_bus
        event_bus.add_listener(EVENT.ORDER,self._match_order)
        
    def get_state(self):
        pass
            
    def set_state(self,state):
        pass
                
    def _match_order(self,event):
        order = event.order
        
        calendar_dt = event.calendar_dt
        trading_dt = event.trading_dt
        ticker = order.ticker
        amount = order.amount
        direction = order.direction
        order_price = order.order_price
        
        # 账户检查是否有充足的股票可以卖出
        if direction == -1:
            available_amount = self.env.account.position.get_position_available(ticker)
            if available_amount >= amount:
                pass
            else:
                amount = available_amount
        # 账户是否有充足的现金买入
        elif direction == 1:
            buy_value = order_price * amount
            cash = self.env.account.cash
            if cash >= buy_value:
                pass
            else:
                cancel_event = Event(EVENT.CANCEL_ORDER,
                                     reason = 'Not enough cash',
                                     ticker = ticker,
                                     amount = amount,
                                     calendar_dt = calendar_dt,
                                     trading_dt = trading_dt)
                self.env.event_bus.publish_event(cancel_event)
                return
                
        # 根据当前bar信息进行撮合
        volume = self.env.data_proxy.get_bar(ticker,calendar_dt)['volume']
        
        # 默认有10倍成交量才能成交
        if volume > 10 * amount:
            match_amount = amount
            match_price = order_price
        else:
            if direction == 1:
                cancel_event = Event(EVENT.CANCEL_ORDER,
                                     reason = 'Not enough stock to buy from',
                                     ticker = ticker,
                                     amount = amount,
                                     calendar_dt = calendar_dt,
                                     trading_dt = trading_dt)
                self.env.event_bus.publish_event(cancel_event)
                return
            elif direction == -1:
                cancel_event = Event(EVENT.CANCEL_ORDER,
                                     reason = 'Not enough stock to sell to',
                                     ticker = ticker,
                                     amount = amount,
                                     calendar_dt = calendar_dt,
                                     trading_dt = trading_dt)
                self.env.event_bus.publish_event(cancel_event)
                return
            
        ## 交易费用
        if direction == -1:
            tax = match_amount * match_price * 0.001
            transfer_fee = int(match_amount/1000) + 1
            commision_fee = max(match_amount * match_price * 0.0003,5)
            transaction_fee = tax + transfer_fee + commision_fee
        elif direction == 1:
            tax = 0
            transfer_fee = int(match_amount/1000) + 1
            commision_fee = max(match_amount * match_price * 0.0003,5)
            transaction_fee = tax + transfer_fee + commision_fee
        
        fill_order_obj = FillOrder(trading_dt,ticker,match_amount,
                                   direction,transaction_fee,
                                   match_price)
        fill_event = Event(EVENT.FILL_ORDER,calendar_dt = calendar_dt,
                           trading_dt = trading_dt,fill_order = fill_order_obj)
        
        self.env.event_bus.publish_event(fill_event)




