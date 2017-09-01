function [target_matrix] = get_history( ticker,start_date,end_date,frequency,kind )
%GET_HISTORY 获取股票历史数据
%  
lib_path = 'G:\Work_ldh\Backtest\VectorTrader\VectorTrader\data\data_source\mixed_data_source\';
NET.addAssembly([lib_path,'FactorsLib2.dll']);

%% 获取数据
start_date_num = datenum(start_date);
end_date_num = datenum(end_date);
target_matrix = [];
if strcmp(frequency(end),'d')
    kind = str2double(kind);
    dayline = FactorsLib2.Factors.DayLine({ticker},start_date_num ,end_date_num ,1,kind); 
    num_time = double(dayline.numtime)';       
    close_price = double(dayline.close);             
    high_price = double(dayline.high);             
    low_price = double(dayline.low);      
    open_price = double(dayline.open);       
    volume = double(dayline.vol);       
    amount = double(dayline.amount);  
    target_matrix = [num_time,open_price,high_price,low_price,close_price,volume,amount];
end
if strcmp(frequency(end),'m')
    onemin = FactorsLib2.OneMinuteLine; 
    cycle = str2double(frequency(1:end-1));
    Openstruct=onemin.KLineOpen({ticker},start_date_num,end_date_num,cycle);
    Highstruct=onemin.KLineHigh({ticker},start_date_num,end_date_num,cycle);
    Lowstruct=onemin.KLineLow({ticker},start_date_num,end_date_num,cycle);
    Closestruct = onemin.KLineClose({ticker},start_date_num,end_date_num,cycle); 
    Volstruct=onemin.KLineVol({ticker},start_date_num,end_date_num,cycle);
    Amountstruct=onemin.KLineAmount({ticker},start_date_num,end_date_num,cycle);
    
    open_price = double(Openstruct.value);
    high_price = double(Highstruct.value);
    low_price = double(Lowstruct.value);
    close_price = double(Closestruct.value);
    volume = double(Volstruct.value);
    amount = double(Amountstruct.value);
    num_time = double(Closestruct.numtime)';
    target_matrix = [num_time,open_price,high_price,low_price,close_price,volume,amount];
end
end

