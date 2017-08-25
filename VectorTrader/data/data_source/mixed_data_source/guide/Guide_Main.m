NET.addAssembly([pwd,'FactorsLib2.dll']);

%% 获取全A股票，获取市场代码，股票名称
scode=cell(FactorsLib2.Factors.getStockcode()); %获取历史全A股票
scode=cell(FactorsLib2.Factors.getStockcode(1)); %剔除退市股票后的全A股票
scode=cell(FactorsLib2.Factors.getStockcode(2)); %剔除退市及ST后的全A股票
stockmarket=cell(FactorsLib2.Factors.getMarket(scode)); %获取输入股票序列的市场代码（输入{'000001'}输出{'SZ'}）
stockname=cell(FactorsLib2.Factors.getStockName(scode)); %获取输入股票代码的股票名（输入{'000001'}输出{'平安银行'}）
scode=cell(FactorsLib2.Factors.SuspensionStock(N,startdate,enddate)); %查询日期内连续停牌超N天的上市A股代码

%% 日线数据
% 详见：
Guide_DayLine

%% 分钟线数据
% 详见：
Guide_1mLine
    
%% 基本面及市场类因子
% 详见：
Guide_FinancialFactors

%% 技术指标因子
% 详见：
Guide_TechFactors





