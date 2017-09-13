# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:44:30 2017

@author: ldh
"""

# convertor.py
            
def df_2_bar_generator(df):
    for (index,series) in df.iterrows():
        yield (index,series)
