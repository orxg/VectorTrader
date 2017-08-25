NET.addAssembly([pwd,'FactorsLib2.dll']);

%% 日线数据(每天17:45更新完)
% 函数参数：DayClose(6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间,是否按上证交易日补全,复权选项);
% 倒数第2个参数：是否按上证交易日补全：0代表按上证交易日输出但不补全，1代表按上证交易日补全，-2代表按自然日排列输出但不补全，-1代表按自然日补全
% 最后1个参数：复权：0代表不复权，1代表后复权，-1代表前复权
% DayOpen,DayHigh,DayLow,DayVol,DayAmount类似

closestruct=FactorsLib2.Factors.DayClose({'000001','000002'},730600,736875,1,-1); % 函数返回数据需按照struct.value  struct.numtime  struct.stockcode  struct.market展开

    close=double(closestruct.value);             %价格数据，行按照numtime排列，列按照stockcode排列
    numtime=double(closestruct.numtime)';        %时间序列
    stockcode=cell(closestruct.stockcode)';      %股票代码序列
    market=cell(closestruct.market)';            %市场代码序列

%% 日线开高低收量价集合
% 参数输入类似DayOpen，函数返回数据需按照struct.value  struct.numtime  struct.stockcode  struct.market展开
dayline=FactorsLib2.Factors.DayLine({'000001','000002'},736600,736875,1,0); 

    numtime=double(dayline.numtime)';        %时间序列
    stockcode=cell(dayline.stockcode)';      %股票代码序列
    market=cell(dayline.market)';            %市场代码序列
    close=double(dayline.close);             %价格数据，行按照numtime排列，列按照stockcode排列，下同
    high=double(dayline.high);             
    low=double(dayline.low);      
    open=double(dayline.open);       
    vol=double(dayline.vol);       
    amount=double(dayline.amount);    