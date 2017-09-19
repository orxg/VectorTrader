# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:23:37 2017

@author: FSB
"""

# simulation_broker.py

from VectorTrader.events import EVENT,Event
from VectorTrader.model.orders import FillOrder

class SimulationBroker():
    def __init__(self,env):
        self.env = env
        self.blotter = []
        
        event_bus = env.event_bus
        event_bus.add_listener(EVENT.PENDING_NEW_ORDER,self._collect_order)
        event_bus.add_listener(EVENT.BAR,self._match_on_bar)
        event_bus.add_listener(EVENT.KILL_ORDER,self._handle_kill_order)
        
    def _collect_order(self,event):
        order = event.order
        self.blotter.append(order)
        self.env.event_bus.publish_event(Event(EVENT.PENDING_NEW_ORDER_PASS,
                                         order = order))
        
    def _match_on_bar(self,event):
        
        while self.blotter: 
            order = self.blotter.pop(0)
            calendar_dt = order.calendar_dt
            trading_dt = order.trading_dt
            ticker = order.ticker
            amount = order.amount
            direction = order.direction
            order_price = order.order_price
            
            # 1. 检查市场是否满足交易条件
            volume = self.env.bar_map.get_latest_bar_value(ticker,'volume')
            # 默认有3倍成交量才能成交
            if volume > 3 * amount:
                match_amount = amount
                match_price = order_price
            else:
                if direction == 1:
                    reject_event = Event(EVENT.REJECT_ORDER,
                                         reason = 'Not enough stock to buy from',
                                         order = order)
                    self.env.event_bus.publish_event(reject_event)
                    return
                elif direction == -1:
                    reject_event = Event(EVENT.REJECT_ORDER,
                                         reason = 'Not enough stock to sell to',
                                         order = order)
                    self.env.event_bus.publish_event(reject_event)
                    return   
                
            # 2. 计算交易费用
            if direction == -1:
                tax = match_amount * match_price * 0.001
                transfer_fee = int(match_amount/1000 - 0.001) + 1
                commission_fee = max(match_amount * match_price * 0.003,5)
                transaction_fee = tax + transfer_fee + commission_fee
            elif direction == 1:
                tax = 0
                transfer_fee = int(match_amount/1000 - 0.001) + 1
                commission_fee = max(match_amount * match_price * 0.003,5)
                transaction_fee = tax + transfer_fee + commission_fee
                
            # 3. 检查账户是否满足交易条件
            ## 账户检查是否有充足的股票可以卖出
            if direction == -1:
                available_amount = self.env.account.position.get_position_available(ticker)
                if available_amount >= amount:
                    pass
                else:
                    amount = available_amount
                    
            ## 账户是否有充足的现金买入
            elif direction == 1:
                buy_value = order_price * amount + transaction_fee
                cash = self.env.account.cash
                if cash >= buy_value:
                    pass
                else:
                    reject_event = Event(EVENT.REJECT_ORDER,
                                         reason = 'Not enough cash',
                                         order = order)
                    self.env.event_bus.publish_event(reject_event)
                    return
            
            # 4. 生成交易反馈            
            fill_order_obj = FillOrder(calendar_dt,trading_dt,
                                       ticker,match_amount,
                                       direction,tax,
                                       commission_fee,transfer_fee,
                                       transaction_fee,
                                       match_price)
            trade_event = Event(EVENT.TRADE,calendar_dt = calendar_dt,
                               trading_dt = trading_dt,order = fill_order_obj)
            
            self.env.event_bus.publish_event(trade_event) 
            
    def _handle_kill_order(self,event):
        '''
        需要实现订单id属性,此处暂不实现。
        '''
        pass
    
        
        
        
    