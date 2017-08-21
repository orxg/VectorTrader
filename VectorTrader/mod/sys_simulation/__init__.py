# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:27:23 2017

@author: ldh
"""

# __init__.py

def load_mod():
    from .mod import SimulationMod
    return SimulationMod()

