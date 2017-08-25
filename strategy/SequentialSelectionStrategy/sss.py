# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:58:59 2017

@author: ldh
"""

# sss.py

from VectorTrader.api import *
import pandas as pd

def initilize(context):
    context.factor_list = ['市值','pe','预计下一年净利润增长率','预计当年净利润增长率',
                           '行业pe','long-term D/E','行业long-term D/E']

def handle_bar(context):
    previous_date = context.previous_date
    universe = context.universe
    factors = []
    
    # 获取因子数据
    for ticker in universe:
        ticker_factor = []
        for factor_name in context.factor_list:
            ticker_factor.append(context.get_factor(factor_name,ticker,previous_date))
        factors.append(ticker_factor)
    data = pd.DataFrame(factors,index = universe,columns = context.factor_list)
    
    # 筛选
    ## 选取市值前30%
    data = data.sort_values(by = '市值',ascending = False)
    num = len(data)
    num = int(0.3 * num)
    data = data.iloc[:num,:]
    ## 选取pe小于行业pe
    data = data.loc[data['pe'] < data['行业pe']]
    
    ## 选取下一年增长率更多
    data = data.loc[data['预计下一年净利润增长率'] > data['预计当年净利润增长率']]
    
    ## 选取财务稳健
    data = data.loc[data['long-term D/E'] < data['行业long-term D/E']]
    
    ## 确定股票池
    target_universe = data.index.values
    
    ## 确定权重
    target_universe_weight = context.calculate_weights()
    
    ## 确定买卖比例
    
    ## 下单操作
    
    
    
            
    
        
    
    

