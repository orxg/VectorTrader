function [ symbols ] = get_symbols()
%GET_SYMBOLS 获取全A数据
%   此处显示详细说明
lib_path = 'G:\Work_ldh\Backtest\VectorTrader\VectorTrader\data\data_source\guosen\';
NET.addAssembly([lib_path,'FactorsLib2.dll']);
symbols =cell(FactorsLib2.Factors.getStockcode());
end

