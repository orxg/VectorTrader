# VectorTrader
个人量化研究。仅能在机构内部使用。

# 远期计划
1. 支持完整的混合数据源
2. 回测、模拟、实盘实现以及便捷切换(同一套代码)
3. 针对多因子策略的定制:因子有效性检验;组合权重;股票收益率建模
4. 分钟、tick级策略
5. 暴露的回测/模拟/交易api,单独暴露的数据api

# update log
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

# update plan
## 2017-08-25
1. 暴露数据api、策略编写过程中的其他api提示
2. 编写序贯选股策略、均线策略，根据编写中的需求更新context，universe等设定，目标是实现序贯选股策略的每日运行与信号发送

## 2017-08-23
1. 加入Wind数据库

## 2017-08-22
1. 整理用户接口，进行整合
2. 增加模拟交易功能

# Installation
1. 要向site-package中加入mod和VectorTrader的路径

