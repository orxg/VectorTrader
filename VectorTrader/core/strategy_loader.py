# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:09:26 2017

@author: ldh
"""

# strategy_loader.py

import six
import codecs

class StrategyLoader():
    
    def __init__(self,strategy_path):
        '''
        加载用户的策略。
        '''
        self.strategy_path = strategy_path
        
    def load(self,scope):
        '''
        读取用户策略。
        
        Parameters
        -----------
            scope
                dict,装载用户策略的空间,namespace
            strategy_path
                用户策略所在路径
                
        Returns
        --------
            scope
                dict,装载用户策略的空间,namespace
        '''
        with codecs.open(self.strategy_path,encoding='utf8') as f:
            source_codes = f.read()
        try:
            source_codes = source_codes.encode('utf8')
        except:
            print 'source codes encoding error,not utf8'
            raise
        source_codes_compiled = compile(source_codes,'strategy.py','exec')
        six.exec_(source_codes_compiled,scope)
        return scope 
       
if __name__ == '__main__':
    strategy_path = '.../test/test_buy_and_hold.py'
    strategy_loader = StrategyLoader(strategy_path)