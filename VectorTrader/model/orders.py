# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:16:27 2017

@author: LDH
"""

# orders.py

class Order():

    def __init__(self,calendar_dt,trading_dt,ticker,
                 amount,direction,order_price):
        '''
        Parameters
        ----------
            calendar_dt
                datetime 交易日日期
            trading_dt
                datetime 交易日时间
            ticker
                股票代码
            amount
                数量
            direction
                方向，买:1,卖-1
            order_price
                出价
        '''
        self.calendar_dt = calendar_dt
        self.trading_dt = trading_dt
        self.ticker = ticker
        self.amount = amount
        self.direction = direction
        self.order_price = order_price
              
    def get_state(self):
        return {'calendar_dt':self.calendar_dt,
                'trading_dt':self.trading_dt,
                'ticker':self.ticker,
                'amount':self.amount,
                'direction':self.direction,
                'order_price':self.order_price}
        
    def set_state(self,state):
        self.calendar_dt = state['calendar_dt']
        self.trading_dt = state['trading_dt']
        self.ticker = state['ticker']
        self.amount = state['amount']
        self.direction = state['direction']
        self.order_price = state['order_price']
        
class FillOrder():
    def __init__(self,calendar_dt,trading_dt,
                 ticker,amount,direction,
                 tax,commission_fee,transfer_fee,
                 transaction_fee,match_price):
        '''
        Parameters
        ----------
            calendar_dt
                datetime,交易日期
            trading_dt
                datetime,交易日期时间
            ticker
                股票代码
            amount
                数量
            direction
                方向，买:1,卖-1
            tax
                税费
            commission_fee
                交易佣金费用
            transfer_fee
                过户费
            transaction_fee
                交易费用
            match_price
                成交价
        '''
        self.calendar_dt = calendar_dt
        self.trading_dt = trading_dt
        self.ticker = ticker
        self.amount = amount
        self.direction = direction
        self.tax = tax
        self.commission_fee = commission_fee
        self.transfer_fee = transfer_fee
        self.transaction_fee = transaction_fee
        self.match_price = match_price
        
    def get_state(self):
        return {'calendar_dt':self.calendar_dt,
                'trading_dt':self.trading_dt,
                'ticker':self.ticker,
                'amount':self.amount,
                'direction':self.direction,
                'tax':self.tax,
                'commission_fee':self.commission_fee,
                'transfer_fee':self.transfer_fee,
                'transaction_fee':self.transaction_fee,
                'match_price':self.match_price}
        
    def set_state(self,state):
        self.calendar_dt = state['calendar_dt']
        self.trading_dt = state['trading_dt']
        self.ticker = state['ticker']
        self.amount = state['amount']
        self.direction = state['direction']
        self.tax = state['tax']
        self.commission_fee = state['commission_fee']
        self.transfer_fee = state['transfer_fee']
        self.transaction_fee = state['transaction_fee']
        self.match_price = state['match_price']
   