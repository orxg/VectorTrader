function [target_matrix] = get_factor( factor_name,ticker,start_date,end_date)
%GET_FACTOR 此处显示有关此函数的摘要
%   此处显示详细说明
lib_path = 'G:\Work_ldh\Backtest\VectorTrader\VectorTrader\data\data_source\mixed_data_source\';
NET.addAssembly([lib_path,'FactorsLib2.dll']);

%% 转换日期
start_date_num = datenum(start_date);
end_date_num = datenum(end_date);    

%% 资产负债率
% 函数参数：AssetToLiabilityRatio(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.AssetToLiabilityRatio({'000001','000002'},727200,736875);
value=double(struct.value);             %因子数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
%% 每股净资产
% 函数参数：NetAssetsPerShare(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.NetAssetsPerShare({'000001','000002'},727200,736875);

%% 净资产收益率ROE
% 函数参数：ROE(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.ROE({'000001','000002'},727200,736875);

%% 销售毛利率
% 函数参数：GrossProfitRatio(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.GrossProfitRatio({'000001','000002'},727200,736875);

%% 净利润,TTM
% 函数参数：NetProfit(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.NetProfit({'000001','000002'},727200,736875);

%% 净利润TTM增长率
% 函数参数：GrowthRateOfNetProfit(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.GrowthRateOfNetProfit({'000001','000002'},727200,736875);

%% 营业总收入增长率
% 函数参数：GrowthRateOfTotalOperatingProfit(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.GrowthRateOfTotalOperatingProfit({'000001','000002'},727200,736875);

%% 每股经营现金流
% 函数参数：CashFlowFromOperationsPerShare(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.CashFlowFromOperationsPerShare({'000001','000002'},727200,736875);

%% 市盈率
% 函数参数：PE(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.PE({'000001','000002'},727200,736875);

%% 市净率
% 函数参数：PB(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.PB({'000001','000002'},727200,736875);

%% 市销率
% 函数参数：PS(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.PS({'000001','000002'},727200,736875);

%% 股息率
% 函数参数：DividendYieldRatio(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.DividendYieldRatio({'000001','000002'},727200,736875);

end

