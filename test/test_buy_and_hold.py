# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:30:40 2017

@author: ldh
"""

# test_buy_and_hold.py

def initilize(context):
    context.fired = False

def handle_bar(context):
    if not context.fired:
        order('600340',100,1)
        context.fired = True
