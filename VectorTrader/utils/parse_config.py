# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 14:48:39 2017

@author: ldh
"""

# parse_config.py
from ..data.data_source.mixed_data_source.mixed_data_source import \
                                                    MixedDataSource

class Config(object):
    
    def __init__(self,config):
        self.config = config
        self.data_source = MixedDataSource()
        self.parse_universe()
        
    @property
    def start_date(self):
        return self.config['base']['start_date']
    
    @property
    def end_date(self):
        return self.config['base']['end_date']
    
    @property
    def capital(self):
        return self.config['base']['capital']
    
    @property
    def frequency(self):
        return self.config['base']['frequency']
        
    def parse_universe(self):
        universe = self.config['base']['universe']
        if len(universe) < 1:
            return []
        else:
            symbol = universe[0]
            if symbol in ['A','hs300','A-st','sz50']:
                self.universe = self.data_source.get_symbols(symbol)
            else:
                self.universe = universe
       
    
        

