# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:11:54 2017

@author: ldh
"""

# account.py

import pickle
from .position import Position
from ..events import EVENT

class Account():
    
    def __init__(self,env,cash):
        
        self.env = env
        
        self.cash = cash
        self.position = Position()
        self.total_account_value = self.cash
        
        self.order_passed = []
        self.order_canceled = []
            
        self.env.event_bus.add_listener(EVENT.TRADE,self._handle_fill_order)
        self.env.event_bus.add_listener(EVENT.PRE_BEFORE_TRADING,self._refresh_pre_before_trading)
        self.env.event_bus.add_listener(EVENT.POST_BAR,self._refresh_post_bar) # 确保第一个接收事件
        self.env.event_bus.add_listener(EVENT.SETTLEMENT,self._refresh_settlement)
        
    def get_state(self):
        state_data = {'cash':self.cash,
                      'total_account_value':self.total_account_value,
                      'position':self.position.get_state(),
                      'order_passed':self.order_passed,
                      'order_canceled':self.order_canceled}
        state_data = pickle.dumps(state_data)
        return state_data
            
    def set_state(self,state):
        state = pickle.loads(state)
        self.cash = state['cash']
        self.total_account_value = state['total_account_value']
        self.position.set_state(state['position'])
        self.order_passed = state['order_passed']
        self.order_canceled = state['order_canceled']
            
    def set_position(self,position_base,cost_base):
        '''
        初始化仓位。
        '''
        self.position.set_init_position(position_base,cost_base)
        self.total_account_value = self.cash + self.position.get_position_value()
        
    def _handle_fill_order(self,event):
        '''
        仅对仓位和成本进行调整。对市场价值和资产总值不做调整。
        '''
        fill_order = event.order
         
        ticker = fill_order.ticker
        match_price = fill_order.match_price
        amount = fill_order.amount
        direction = fill_order.direction
        transaction_fee = fill_order.transaction_fee
        
        origin_position = self.position.get_position(ticker)
        
        new_position = origin_position + direction * amount
        
        self.cash += - direction * amount * match_price - transaction_fee
        self.position.set_position(ticker,new_position)      
        self.order_passed.append((event.calendar_dt,event.trading_dt,
                                  ticker,amount,direction,match_price,
                                  transaction_fee))
        
    def _refresh_pre_before_trading(self,event):
        data_proxy = self.env.data_proxy
        
        ## TODO:优化算法(可读性与效率)
        for ticker in self.env.get_universe():
            
            # 获取分红配股数据
            dividend = data_proxy.get_pre_before_trading_dividend(ticker,self.env.calendar_dt)
            rights_issue = data_proxy.get_pre_before_trading_rights_issue(ticker,self.env.calendar_dt)
            
            # 处理分红
            if dividend is not 0:
                dividend_per_share = dividend['dividend_per_share']
                multiplier = dividend['multiplier']
                self.cash += self.position.get_position(ticker) * dividend_per_share
                self.position.set_position(ticker,self.position.get_position(ticker) * multiplier)
                
            # 处理配股
            if rights_issue is not 0:
                rights_issue_per_stock = rights_issue['rights_issue_per_stock']
                rights_issue_price = rights_issue['rights_issue_price']
                transfer_rights_issue_per_stock = rights_issue['transfer_rights_issue_per_stock']
                transfer_rights_issue_price = rights_issue['transfer_rights_issue_price']
                current_position = self.position.get_position(ticker)
                rights_issue_stocks = int(rights_issue_per_stock * current_position)
                transfer_rights_issue_stocks = int(transfer_rights_issue_per_stock * current_position)
                
                rights_issue_maximum_cost = rights_issue_stocks * rights_issue_price
                transfer_rights_issue_maximum_cost = transfer_rights_issue_stocks * transfer_rights_issue_price
                
                # 配股逻辑
                # 原则:有钱就配,能配多少是多少
                ## XXX : 写的太多,此处逻辑正确性未测试
                if transfer_rights_issue_price == 0:
                    
                    if self.cash >= rights_issue_maximum_cost:
                        self.cash -= rights_issue_maximum_cost
                        self.position.add_position(ticker,rights_issue_stocks)
                    elif self.cash < rights_issue_maximum_cost:
                        
                        rights_issue_stocks = int(self.cash / rights_issue_price)
                        self.cash -= rights_issue_stocks * rights_issue_price
                        self.position.add_position(ticker,rights_issue_stocks)
                elif transfer_rights_issue_price > 0:
                    
                    if self.cash >= (rights_issue_maximum_cost + \
                                     transfer_rights_issue_maximum_cost):
                        self.cash -= rights_issue_maximum_cost + \
                                    transfer_rights_issue_maximum_cost
                        self.position.add_position(ticker,rights_issue_stocks + \
                                                   transfer_rights_issue_stocks)
                    elif self.cash < (rights_issue_maximum_cost + \
                                      transfer_rights_issue_maximum_cost) and \
                         self.cash >= rights_issue_maximum_cost:
                             
                        self.cash -= rights_issue_stocks * rights_issue_price
                        self.position.add_position(ticker,rights_issue_stocks)
                        transfer_rights_issue_stocks = int(self.cash / transfer_rights_issue_price)
                        self.cash -= transfer_rights_issue_stocks * transfer_rights_issue_price
                        self.position.add_position(ticker,transfer_rights_issue_stocks)
                    elif self.cash < rights_issue_maximum_cost:
                        
                        rights_issue_stocks = int(self.cash / rights_issue_price)
                        self.cash -= rights_issue_stocks * rights_issue_price
                        self.position.add_position(ticker,rights_issue_stocks)
        
    def _refresh_post_bar(self,event):
        for ticker,value in self.position.position.items():
            close_price = self.env.bar_map.get_latest_bar_value(ticker)
            self.position.set_position_market_value(ticker,value * close_price)
        self.total_account_value = self.cash + self.position.get_position_value()
        
    def _refresh_settlement(self,event):
        '''
        更新可卖证券。
        '''
        for ticker,value in self.position.position.items():
            self.position.set_position_available(ticker,value)
            

    
            
        
        
            
        
        
        
        