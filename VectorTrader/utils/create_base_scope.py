# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:18:59 2017

@author: ldh
"""

# create_base_scope.py
import copy

def create_base_scope():
    from .. import user_base_scope
    scope = copy.copy(user_base_scope.__dict__)
    return scope
