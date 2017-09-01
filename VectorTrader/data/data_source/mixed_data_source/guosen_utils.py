# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:21:49 2017

@author: ldh
"""

# guosen_utils.py

import datetime
import pandas as pd
import pymssql
from utils import convert_time,convert_to_float

server = '172.19.62.183'
user = 'DataAdmin'
password = 'fs95536!'
con = pymssql.connect(server,user,password,'BasicData',charset='utf8')
cur = con.cursor()

def get_dividend(ticker,start_date,end_date):
    '''
    获取股票时间段内实施的分红送股转增数据。
    Parameters
    ----------
        ticker
            '600340'
        start_date
            '20100101'
        end_date
            '20150101'
    Returns
    --------
        DataFrame
            index XD_date
            columns XD_date,dividend_per_share,multiplier
                    (除权除息日,每股分红,分红后每股乘数)
    '''
    sql_select = '''
    SELECT [stockcode]
      ,[除权除息日]
      ,[送股比例分子]
      ,[转增比例分子]
      ,[派息比例分子_税后]
    FROM BasicData.dbo.Yi_Dividend 
    WHERE stockcode = '%s'
    AND [numtime] is not Null
    '''%(ticker)
    cur.execute(sql_select)
    data = cur.fetchall()
    columns = ['ticker', 'XD_date','stock_dividend_numerator',
               'transfer_numerator','cash_dividend_numerator_after_tax']
    
    df = pd.DataFrame(data,columns = columns)
    df = df.fillna(0)
    df['dividend_per_share'] = convert_to_float(df[u'cash_dividend_numerator_after_tax']) / 10.0
    df['multiplier'] = 1 + (convert_to_float(df[u'stock_dividend_numerator']) + \
                                                  convert_to_float(df[u'transfer_numerator'])) / 10.0
    df['XD_date'] = convert_time(df['XD_date'])
    df = df[['XD_date','dividend_per_share','multiplier']].set_index('XD_date',drop = False)
    df = df.sort_index()
    df = df[start_date:end_date]
    return df

def get_rights_issue(ticker,start_date,end_date):
    '''
    获取股票已实施配股数据。
    Parameters
    ----------
        ticker
            '600340'
        start_date
            '20100101'
        end_date
            '20150101'
    Returns
    --------
        DataFrame
            index ex_rights_date
            columns 
                'ex_rights_date','rights_issue_per_stock','rights_issue_price',
                'transfer_rights_issue_per_stock','transfer_price'
                    (除权日,每股配股,配股价，每股转配，每股转配价)
    '''
    sql_select = '''
    SELECT [除权日]
      ,[配股比例分子]
      ,[配股价格]
      ,[转配比例分子]
      ,[转让费]
      FROM [BasicData].[dbo].[Yi_RightsIssue]
      WHERE [除权日] is not null
      AND [stockcode] = '%s'
    '''%(ticker)
    cur.execute(sql_select)
    data = cur.fetchall()
    columns = ['ex_rights_date','rights_issue_numerator','rights_issue_price',
               'transfer_rights_issue_numerator','transfer_rights_issue_fee']
    df = pd.DataFrame(data,columns = columns)
    df = df.fillna(0)
    df['ex_rights_date'] = convert_time(df['ex_rights_date'])
    df['rights_issue_price'] = convert_to_float(df['rights_issue_price'])
    df['rights_issue_per_stock'] = \
            convert_to_float(df['rights_issue_numerator']) / 10.0
    df['transfer_rights_issue_per_stock'] = \
            convert_to_float(df['transfer_rights_issue_numerator']) / 10.0
    df['transfer_price'] = \
            df['rights_issue_price'] + convert_to_float(df['transfer_rights_issue_fee'])
    df = df[['ex_rights_date','rights_issue_per_stock','rights_issue_price',
             'transfer_rights_issue_per_stock','transfer_price']]
    df = df.set_index('ex_rights_date',drop = False)
    df = df.sort_index()
    df = df[start_date:end_date]
    return df
    

def get_trade_status(ticker,start_date,end_date):
    '''
    获取股票交易状态。
    Parameters
    -----------
        ticker
            股票代码
        start_date
            '20100101'
        end_date
            '20150101'
    Returns
    --------
        DataFrame 
            index date_time
            columns (date_time,ticker,status)
    Notes
    -------
        status 
            正常交易: 1
            停牌: 0
    '''
    sql_select = '''
    SELECT [numtime]
          ,[stockcode]
          ,[value]
    FROM [BasicData].[dbo].[Yi_TradeState]
    WHERE [stockcode] = '%s'
    '''%(ticker)
    cur.execute(sql_select)
    data = cur.fetchall()
    columns = ['date_time','ticker','status']
    df = pd.DataFrame(data,columns = columns)
    df['date_time'] = convert_time(df['date_time'])
    df = df.set_index('date_time',drop = False)
    df = df.sort_index()
    df['status'] = df['status'].apply(lambda x : 1 if x != 0 else 0)
    df = df[start_date:end_date]
    return df

def get_list_delist_date(ticker):
    '''
    获取股票上市与退市日期。若没有退市，则退市为0.
    Parameters
    -----------
        ticker
            600340
    Returns
    --------
        tuple
            (list_date,delist_date) datetime类型
    '''
    sql_select = '''
    SELECT  [股票代码]
      ,[上市日期]
      ,[摘牌日期]
    FROM [BasicData].[dbo].[Yi_Stocks]
    WHERE [股票代码] = '%s'
    '''%(ticker)
    cur.execute(sql_select)
    data = cur.fetchall()
    list_date = datetime.datetime.strptime(data[0][1],'%Y%m%d')
    if data[0][2] is not None:
        delist_date = datetime.datetime.strptime(data[0][2],'%Y%m%d')
    else:
        delist_date = 0
    return list_date,delist_date


if __name__ == '__main__':
    ticker = '000001'
    start_date = '20150101'
    end_date = '20150501'
    
    dividend = get_dividend(ticker,start_date,end_date)
    rights_issue = get_rights_issue(ticker,start_date,end_date)
    trade_status = get_trade_status(ticker,start_date,end_date)
    list_delist = get_list_delist_date(ticker)
    
    print dividend.head()
    print rights_issue.head()
    print trade_status.head()
    print list_delist
    

