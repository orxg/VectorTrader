# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:16:27 2017

@author: LDH
"""

# orders.py

class Order():
    def __init__(self,dt,ticker,amount,direction,order_price):
        '''
        Parameters
        ----------
            dt
                datetime
            ticker
                股票代码
            amount
                数量
            direction
                方向，买:1,卖-1
            order_price
                出价
        '''
        self.dt = dt
        self.ticker = ticker
        self.amount = amount
        self.direction = direction
        self.order_price = order_price
        
# --------------------- Abandon Method---------------------        
    def get_state(self):
        return {'dt':self.dt,
                'ticker':self.ticker,
                'amount':self.amount,
                'direction':self.direction,
                'order_price':self.order_price}
        
    def set_state(self,state):
        self.dt = state['dt']
        self.ticker = state['ticker']
        self.amount = state['amount']
        self.direction = state['direction']
        self.order_price = state['order_price']
        
class FillOrder():
    def __init__(self,dt,ticker,amount,direction,transaction_fee,match_price):
        '''
        Parameters
        ----------
            dt
                datetime
            ticker
                股票代码
            amount
                数量
            direction
                方向，买:1,卖-1
            transaction_fee
                交易费用
            match_price
                成交价
        '''
        self.dt = dt
        self.ticker = ticker
        self.amount = amount
        self.direction = direction
        self.transaction_fee = transaction_fee
        self.match_price = match_price
        
# --------------------- Abandon Method---------------------
    def get_state(self):
        return {'dt':self.dt,
                'ticker':self.ticker,
                'amount':self.amount,
                'direction':self.direction,
                'transaction_fee':self.transaction_fee,
                'match_price':self.order_price}
        
    def set_state(self,state):
        self.dt = state['dt']
        self.ticker = state['ticker']
        self.amount = state['amount']
        self.direction = state['direction']
        self.transaction_fee = state['transaction_fee']
        self.match_price = state['match_price']
   