# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:57:28 2017

@author: ldh
"""

# utils.py
import datetime as dt

def time_to_market_date_convertor(date):
    try:
        time_to_market = dt.datetime.strptime(str(date),'%Y%m%d')
        return time_to_market
    except:
        return dt.datetime(1991,1,1)
    

def get_last_updated_time(con,table_name):
    '''
    获取上次更新的时间。
    '''
    sql = '''
    SELECT last_updated_time FROM %s LIMIT 1
    '''%table_name
    cur = con.cursor()
    cur.execute(sql)
    last_updated_time = cur.fetchall()[0][0]
    return last_updated_time
