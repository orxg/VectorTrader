# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:16:27 2017

@author: LDH
"""

# orders.py

from ..utils import id_gen

class Order(object):
    
    def __init__(self):
        self._id = None
        self._calendar_dt = None
        self._trading_dt = None
        self._status = None
        
        self._type = None
        self._order_book_id = None
        self._quantity = None
        self._side = None
        self._limit_price = None
        self._frozen_price = None
        
        self._filled_quantity = None
        
        self._tax = None
        self._commision_fee = None
        self._transfer_fee = None
        self._transaction_cost = None
        
    def get_state(self):
        return {
                'id':self.id,
                'calendar_dt':self._calendar_dt,
                'trading_dt':self._trading_dt,
                'side':self._side,
                }
        
        
   