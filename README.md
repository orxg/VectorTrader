# VectorTrader
量化研究。

# Installation
1. 向site-packages中添加VectorTrader路径文件pth.
2. 安装requirments中的需求
3. 在data_source中的mixed_data_source中根据Readme进行调整。

# update log
## 2017-09-01
1. 更真实的回测(不复权数据 + 分红送股 + 配股;动态股票池，每日自动剔除未上市、停牌、退市股票)
2. 修改了回测取数据的方法，不再采用bar数据结构，不再采用history_bar对象，其功能整合到context中。

## 2017-08-31
1. 增加了一些国信本地数据接口(分红送转，停牌，上市退市，配股转配股)
2. get_history支持分钟线数据

## 2017-08-29
1. 美化资金曲线的输出
2. 增加T+1交易机制
3. 优化撮合机制以及手续费
4. 增加订单记录

## 2017-08-28
1. 在modlue中增加了Calendar，提供日期滑动的功能(目前支持19910101到回测截止日期的滑动)
2. 在core中添加HistoryBars负责提供回测中的可得历史行情数据。
3. 在utils中添加convertor,提供bar与dataframe的转换
4. 修改dataproxy准备回测数据的逻辑，将通过时间取数据改成用生成器产生对应数据(重要改动)
5. get_bar仅能通过bar_map调用,所以api中的下单函数采用data_proxy的新增函数get_price获取对应的价格数据
6. 通过5日均线与30日均线策略的测试
7. 在analyser中增加了收益率统计、保存、展示功能(对应修改了main)
8. account更新的触发事件，改为POST_BAR

## 2017-08-25
1. 建立了部分基于Wind的数据库(不能正常使用)
2. 建立了基于本地数据库的数据接口(基于matlab引擎)，未测试
3. 建立最新混合数据源(MixedDataSource)，该数据源以本地数据库为基础，结合tushare,wind等数据接口，功能强大，通过buy_and_hold策略测试。
4. 更改默认数据源为混合数据源。
5. 增加了一些数据接口相关的工具函数(wind_utils,matlab_utils,tushare_utils,utils等)。
6. 增加更多相关数据代理函数。

## 2017-08-23
1. 加入进度条mod，在cmd模式下可以正常运行
2. 加入了模拟交易mod,功能尚未测试
3. 优化了mod管理

## 2017-08-22
程序成功运行单只股票buy_and_hold策略。

# Issue
## Issue 01(解决)
1. 当股票池为2017新股的时候，仍然在2014年有交易不成功的记录
2. 在不符合交易逻辑的情况下进行了买入
3. 做的图是一个白图，里面什么都没有
