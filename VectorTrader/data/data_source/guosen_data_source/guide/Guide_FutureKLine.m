%% 获取期货分钟线或基于分钟线合成的各种周期K线
NET.addAssembly([pwd,'FactorsLib2.dll']);
future=FactorsLib2.FutureData; % 实例化

%% 获取期货历史一分钟K线
cycle=[3,15,240]; %周期，单位分钟，可同时获取多个周期的K线
Closestruct=future.KLineClose(codes,startdate,enddate,cycle); % cycle=1或不输入cycle参数可获取1分钟线（前复权）
    % 单个周期或1分钟线的情况下，输出Closestruct为struct格式：
        close=double(Closestruct.value);             %价格数据，行按照numtime排列，列按照stockcode排列
        numtime=double(Closestruct.numtime)';        %时间序列
        stockcode=cell(Closestruct.stockcode)';      %合约代码序列
    % 多个周期的情况下，输出Closestruct为struct数组格式：(以下代码输出第一个周期的数据)
        close=double(Closestruct(1).value);             %价格数据，行按照numtime排列，列按照stockcode排列
        numtime=double(Closestruct(1).numtime)';        %时间序列
        stockcode=cell(Closestruct(1).stockcode)';      %合约代码序列
        
   
        Openstruct=future.KLineHigh(codes,startdate,enddate,cycle);
        Highstruct=future.KLineHigh(codes,startdate,enddate,cycle);
        Lowstruct=future.KLineLow(codes,startdate,enddate,cycle);
        Volstruct=future.KLineVol(codes,startdate,enddate,cycle);
        Amountstruct=future.KLineAmount(codes,startdate,enddate,cycle);
        OpenIntereststruct=future.KLineOpenInterest(codes,startdate,enddate,cycle);