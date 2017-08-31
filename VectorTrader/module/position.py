# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:46:23 2017

@author: ldh
"""

# position.py

class Position():
    def __init__(self):
        self.position = {}
        self.position_available = {}
        self.position_market_value = {}
        
    def get_position(self,ticker):
        try:
            return self.position[ticker]
        except:
            return 0
    
    def get_position_available(self,ticker):
        try:
            return self.position_available[ticker]
        except:
            return 0        

        
    def get_position_market_value(self,ticker):
        try:
            return self.position_market_value[ticker]
        except:
            return 0     
        
    def get_position_value(self):
        total_value = 0
        for name,value in self.position_market_value.items():
            total_value += value
        return total_value
    
    def set_position(self,ticker,shares):
        self.position[ticker] = shares
        
    def set_position_available(self,ticker,shares):
        self.position_available[ticker] = shares
        
    def set_position_market_value(self,ticker,value):
        self.position_market_value[ticker] = value
    
    def add_position(self,ticker,shares):
        try:
            self.position[ticker] += shares
        except:
            self.position[ticker] = shares
    
