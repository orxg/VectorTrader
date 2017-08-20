# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:56:01 2017

@author: ldh
"""

# tushare_data_source.py

import pymysql
import pandas as pd

class TushareDataSource():
    '''
    基于tushare的数据源接口。
    '''
    def __init__(self):
        self.host = 'localhost'
        self.user = 'sec_user'
        self.passwd = '123456'
        self.db = 'securities'
        self.con = None
        self.start() # 开启接口
        
    def start(self):
        '''
        开启接口。
        '''
        self.con = pymysql.connect(
                self.host,
                self.user,
                self.passwd,
                self.db)
        
    def get_daily_trading_data(self,ticker,start_date,end_date):
        '''
        获取日间交易数据。
        Parameters
        -----------
            ticker
                '600340'
            start_date
                '20160101'
            end_date
                '20170101'
        Returns
        --------
            DataFrame
                index 
                    pd.Timestamp
                columns
                    open_price,high_price,low_price,close_price,volume(前复权)
                
        '''
        sql = '''
        SELECT dp.date_time,dp.open_price,
        dp.high_price,dp.low_price,dp.close_price,
        dp.volume
        FROM daily_price as dp 
        INNER JOIN symbols as s
        ON dp.stock_id = s.id
        WHERE s.ticker = {ticker}
        AND dp.date_time >= {start_date}
        AND dp.date_time <= {end_date}
        '''.format(ticker = ticker,
        start_date = start_date,
        end_date = end_date)
        
        daily_price_df = pd.read_sql(sql,self.con,parse_dates = ['date_time'])
        return daily_price_df
    
    def get_calendar_days(self,start_date,end_date):
        '''
        获取交易日历
        Returns
        -------
            list [pd.Timestamp]
        '''
        sql = 'SELECT date from tradedates'
        dates = pd.read_sql(sql,self.con,parse_dates = ['date'])['date']
        return dates[start_date:end_date].tolist()