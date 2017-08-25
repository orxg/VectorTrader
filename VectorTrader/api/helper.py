# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:19:05 2017

@author: ldh
"""

# helper.py

from . import api

def get_apis():
    apis = {name:getattr(api,name) for name in api.__all__}
    return apis