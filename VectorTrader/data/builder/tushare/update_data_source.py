# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:44:53 2017

@author: ldh
"""

# update_data_source.py

import datetime as dt
from sqlalchemy import create_engine

import pandas as pd
import tushare as ts

from utils import get_last_updated_time

db_host = 'localhost'
db_user = 'sec_user'
db_pass = '123456'
db_name = 'securities' 

con = create_engine('mysql://{user}:{passwd}@{host}/{db}'.format(
        host = db_host,
        user = db_user,
        passwd =db_pass,
        db = db_name),
        charset = 'utf8')

def update():
    '''
    数据更新汇总。
    '''
    update_symbols()
    update_calendar_days()
    update_daily_price_pregened()
    con.close()
    
def update_symbols():
    '''
    更新股票基本信息。
    '''
    now = dt.datetime.now()
    data = ts.get_stock_basics()

    
    data['created_time'] = now
    data['last_updated_time'] = now
    data['id'] = range(1,len(data) + 1)
    data['ticker'] = data.index
    data['timeToMarket'] = data['timeToMarket'].apply(time_to_market_date_convertor)
    data.to_sql('symbols',con,if_exists = 'replace',
                index = False,flavor = 'mysql')
    
    sql = '''
    ALTER TABLE symbols
    ADD PRIMARY KEY (id);
    '''
    
    cur = con.cursor()
    cur.execute(sql)
    con.close()
    print('成功更新symbols表(股票基本信息)')    
    
def update_calendar_days():
    '''
    更新MySQL数据库中的交易日历。
    '''
    start_date = '1990-01-01'
    end_date = dt.date.today().strftime('%Y-%m-%d')
    tradedates = ts.get_k_data('000001',start = start_date,
                               end = end_date,
                               index = True)[['date']]
    
    tradedates.date = pd.to_datetime(tradedates.date)
    now = dt.date.today()
    tradedates['last_updated_time'] = now
    
    con = create_engine('mysql://{user}:{passwd}@{host}/{db}'.format(
            host = db_host,
            user = db_user,
            passwd =db_pass,
            db = db_name),
            charset = 'utf8')
    
    tradedates.to_sql('tradedates',con,flavor = 'mysql',
                          if_exists = 'replace')
        
    print('成功更新交易日历数据tradedates')    

def update_daily_price_pregened():
    '''
    更新股票前复权价格数据
    '''
    last_updated_time = get_last_updated_time(con,'daily_price')
    
    
    pass

if __name__ == '__main__':
    update()
    

