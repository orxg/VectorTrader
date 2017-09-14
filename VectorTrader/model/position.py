# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:46:23 2017

@author: ldh
"""

# position.py

from collections import defaultdict

class Position():
    def __init__(self):
        self.position = {}
        self.position_available = {}
        self.position_cost = {}
        self.position_lot = defaultdict(list)
        self.position_market_value = {}
        
    def get_state(self):
        state_data = {'position':self.position,
                      'position_available':self.position_available,
                      'position_cost':self.position_cost,
                      'position_lot':self.position_lot,
                      'position_market_value':self.position_market_value}
        return state_data
    
    def set_state(self,state):
        self.position = state['position']
        self.position_available = state['position_available']
        self.position_cost = state['position_cost']
        self.position_lot = state['position_lot']
        self.position_market_value = state['position_market_value']
                
    def set_init_position(self,position_base,cost_base):
        for key,value in position_base.items():
            self.position[key] = value
            self.position_available[key] = value
        for key,value in cost_base.items():
            self.position_cost[key] = value
            
    def get_holding_universe(self):
        universe = []
        for key,value in self.position.items():
            if value != 0:
                universe.append(key)
        return universe
    
    def get_holding_available_universe(self):
        universe = []
        for key,value in self.position_available.items():
            if value != 0:
                universe.append(key)
        return universe        
        
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
    
    def __getitem__(self,ticker):
        return self.get_position(ticker)