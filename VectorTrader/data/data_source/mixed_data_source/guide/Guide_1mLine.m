%% 获取分钟线或基于分钟线合成的各种周期K线
NET.addAssembly([pwd,'FactorsLib2.dll']);
scc=cell(FactorsLib2.Factors.getStockcode(1)); %全A非退市股票代码
onemin=FactorsLib2.OneMinuteLine; % 实例化

%% 获取截止到昨日的前复权K线
cycle=[3,15,240]; %周期，单位分钟，可同时获取多个周期的K线
Closestruct=onemin.KLineClose(scc,startdate,enddate,cycle); % cycle=1或不输入cycle参数可获取1分钟线（前复权）
    % 单个周期或1分钟线的情况下，输出Closestruct为struct格式：
        close=double(Closestruct.value);             %价格数据，行按照numtime排列，列按照stockcode排列
        numtime=double(Closestruct.numtime)';        %时间序列
        stockcode=cell(Closestruct.stockcode)';      %股票代码序列
        market=cell(Closestruct.market)';            %市场代码序列
    % 多个周期的情况下，输出Closestruct为struct数组格式：(以下代码输出第一个周期的数据)
        close=double(Closestruct(1).value);             %价格数据，行按照numtime排列，列按照stockcode排列
        numtime=double(Closestruct(1).numtime)';        %时间序列
        stockcode=cell(Closestruct(1).stockcode)';      %股票代码序列
        market=cell(Closestruct(1).market)';            %市场代码序列
        
        
% 提醒：分钟线数据量大，一次性取全A半年分钟线时，电脑的内存使用（32G）便会接近极限，若需更长数据，建议将股票分多个部分取，然后再拼起来

        Openstruct=onemin.KLineOpen(scc,startdate,enddate,cycle);
        Highstruct=onemin.KLineHigh(scc,startdate,enddate,cycle);
        Lowstruct=onemin.KLineLow(scc,startdate,enddate,cycle);
        Volstruct=onemin.KLineVol(scc,startdate,enddate,cycle);
        Amountstruct=onemin.KLineAmount(scc,startdate,enddate,cycle);