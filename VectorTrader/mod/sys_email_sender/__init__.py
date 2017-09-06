# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 15:24:16 2017

@author: ldh
"""

# __init__.py

def load_mod():
    from .mod import EmailSenderMod
    return EmailSenderMod()

