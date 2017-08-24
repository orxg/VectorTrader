# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:55:51 2017

@author: ldh
"""

# build_wind_data_source.py
import datetime as dt
import pandas as pd
import pymysql
from api_wind import *
from utils import convert_to_datetime

host = 'localhost'
user = 'sec_user'
password = '123456'
db = 'securities_wind'

con = pymysql.connect(host,user,password,db,charset = 'utf8')
cur = con.cursor()

def build_symbols():
    sql_create_table = '''
    DROP TABLE IF EXISTS symbols ;
    CREATE TABLE symbols(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ticker varchar(32) NOT NULL,
    sec_name varchar(255) NOT NULL,
    ipo_date datetime NOT NULL,
    total_shares double,
    float_a_shares double,
    free_float_shares double,
    industry_gics varchar(32),
    industry_gicscode varchar(32),
    indexcode_wind varchar(32))engine=InnoDB
    '''
    try:
        cur.execute(sql_create_table)
    except Exception as e:
        print e
        raise
        
    all_A_symbols = get_all_symbols()
    insert_str = ('%s,' * 9)[:-1]
    column_str = '''
    sec_name,ipo_date,total_shares,float_a_shares,free_float_shares,industry_gics,industry_gicscode,indexcode_wind,ticker
    '''
    final_str = 'INSERT INTO symbols (%s) VALUES (%s)'%(column_str,insert_str)
    basics = get_stock_list_basics(all_A_symbols).values.tolist()
    cur.executemany(final_str,basics)
    con.commit()
    print 'Successfully insert the basic information of all A stocks'

def build_trading_days():
    '''
    '''
    today = dt.date.today().strftime('%Y-%m-%d')
    start_date = '1991-01-01'
    end_date = today
    last_updated_date = end_date
    
    
    
    sql_create_table = '''
    DROP TABLE IF EXISTS tradedates;
    CREATE TABLE tradedates (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date_time datetime,
    last_updated_date datetime
    )engine = InnoDB
    '''
    cur.execute(sql_create_table)
    
    trading_days = get_trading_days(start_date,end_date).tolist()
    trading_days = list(convert_to_datetime(trading_days))
    
    schema_list = []
    for each in trading_days:
        schema_list.append([each,last_updated_date])
    
    column_str = 'date_time,last_updated_date'
    insert_str = ('%s,'*2)[:-1]
    final_str = '''
    INSERT INTO tradedates (%s) VALUES (%s)
    '''%(column_str,insert_str)
    
    cur.executemany(final_str,schema_list)
    con.commit()
    
def build_daily_trading():
    
    sql_create_table = '''
    CREATE TABLE daily_price (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ticker_id INT NOT NULL,
    ticker VARCHAR(32),
    date_time datetime,
    open_price double,
    high_price double,
    low_price double,
    close_price double,
    volume double,
    amount double,
    free_turnover_ratio double,
    trade_status varchar(32),
    maxup_or_maxdown int,
    last_updated_datetime datetime)engine = InnoDB
    '''
    cur.execute(sql_create_table)
    
    sql_select_ticker_id = '''
    SELECT id,ticker,ipo_date FROM symbols 
    '''
    cur.execute(sql_select_ticker_id)
    data = cur.fetchall()
    
    column_str = '''
    open_price,high_price,low_price,close_price,volume,amount,
    free_turnover_ratio,trade_status,maxup_or_maxdown,ticker,
    date_time,ticker_id,last_updated_datetime
    '''
    insert_str = ('%s' * 13)[:-1]
    final_str = '''
    INSERT INTO daily_price (%s) VALUES (%s)
    '''%(column_str,insert_str)
    
    total_length = len(data)
    i = 0
    for idx,ticker,ipo_date in data:
        i += 1
        now = dt.datetime.now()
        start_date = ipo_date.strftime('%Y%m%d')
        end_date = now.strftime('%Y%m%d')
        last_updated_datetime = now
        ticker_data = get_stock_daily_price(ticker,start_date,end_date)
        ticker_data['ticker_id'] = idx
        ticker_data['last_updated_datetime'] = now
        ticker_data['date_time'] = convert_to_datetime(ticker_data['date_time'])
        ticker_data['last_updated_datetime'] = convert_to_datetime(ticker_data['last_updated_datetime'])
        ticker_data = ticker_data.values.tolist()
        cur.executemany(final_str,ticker_data)
        print '%s 股票已经成功插入数据库'%ticker
        print '%s/%s'%(i,total_length)
        
if __name__ == '__main__':
    build_daily_trading()
    con.close()

