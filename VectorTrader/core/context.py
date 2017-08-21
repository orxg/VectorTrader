# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:18:32 2017

@author: ldh
"""

# context.py

from ..environment import Environment

class Context():
    def __init__(self):
        pass
        
    @property
    def current_date(self):
        return Environment.get_instance().calendar_dt
    
    ## TODO:更多的属性
    @property
    def previous_date(self):
        pass
    
    @property
    def position(self):
        pass
    
    @property
    def portfolio_value(self):
        pass
    
    
    
    
    
    
