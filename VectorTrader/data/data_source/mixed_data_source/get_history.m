function [target_matrix] = get_history( ticker,start_date,end_date,frequency )
%GET_HISTORY 获取股票历史数据
%  
lib_path = 'G:\Work_ldh\Backtest\VectorTrader\VectorTrader\data\data_source\mixed_data_source\';
NET.addAssembly([lib_path,'FactorsLib2.dll']);

%% 获取数据
start_date_num = datenum(start_date);
end_date_num = datenum(end_date);
target_matrix = []
if frequency == '1d'
    dayline = FactorsLib2.Factors.DayLine({ticker},start_date_num ,end_date_num ,1,-1); 
    num_time=double(dayline.numtime)';        %时间序列
    close_price = double(dayline.close);             
    high_price = double(dayline.high);             
    low_price = double(dayline.low);      
    open_price = double(dayline.open);       
    volume = double(dayline.vol);       
    amount = double(dayline.amount);    
    target_matrix = [num_time,open_price,high_price,low_price,close_price,volume,amount];
end

end

