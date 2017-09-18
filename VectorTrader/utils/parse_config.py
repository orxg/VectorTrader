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
        
    def to_dict(self):
        return self.config
    
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
        
    @property
    def position_base(self):
        if 'position_base' in self.config['base'].keys():
            return self.config['base']['position_base']
        else:
            return None
        
    @property
    def cost_base(self):
        if 'cost_base' in self.config['base'].keys():
            return self.config['base']['cost_base']
        else:
            return None
        
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
       
    
        

