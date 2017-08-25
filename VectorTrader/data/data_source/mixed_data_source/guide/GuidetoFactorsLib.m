NET.addAssembly('D:\FactorsLib2.dll');

%% 获取全A股票，获取市场代码，股票名称
scode=cell(FactorsLib2.Factors.getStockcode()); %获取全A股票
scode=cell(FactorsLib2.Factors.getStockcode(1)); %剔除退市股票后的全A股票
stockmarket=cell(FactorsLib2.Factors.getMarket(scode)); %获取输入股票序列的市场代码
stockname=cell(FactorsLib2.Factors.getStockName(scode)); %获取输入股票序列的中文简称

%% 日线数据(每天17:45更新完)
% 函数参数：DayClose(6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间,是否按上证交易日补全,复权选项);
% 是否按上证交易日补全：1代表按上证交易日补全，-1代表按自然日补全，0代表不补全，-2代表按自然日排列但不补全
% 复权：0代表不复权，1代表后复权，-1代表前复权
% DayOpen,DayHigh,DayLow,DayVol,DayAmount类似

struct=FactorsLib2.Factors.DayClose({'000001','000002'},730600,736875,1,-1); % 函数返回数据需按照struct.value  struct.numtime  struct.stockcode  struct.market展开
struct2=FactorsLib2.Factors.DayClose(scode,730600,today,0,0);

value=double(struct.value);             %价格数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

%% 日线开高低收量价集合
% 参数输入类似DayOpen，函数返回数据需按照struct.value  struct.numtime  struct.stockcode  struct.market展开
dayline=FactorsLib2.Factors.DayLine({'000001','000002'},736600,736875,1,0); 

numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列
close=double(struct.close);             %价格数据，行按照numtime排列，列按照stockcode排列，下同
high=double(struct.high);             
low=double(struct.low);      
open=double(struct.open);       
vol=double(struct.vol);       
amount=double(struct.amount);    

%% 均线MA
% 函数参数：MA(均线周期,6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间,是否按上证交易日补全,复权选项);
% 是否按上证交易日补全：1代表按上证交易日补全，-1代表按自然日补全，0代表不补全，-2代表按自然日排列但不补全
% 复权：0代表不复权，1代表后复权，-1代表前复权

struct=FactorsLib2.Factors.MA(5,{'000001','000002'},730600,736875,1,-1); % 函数返回收盘价5日均线数据

value=double(struct.value);             %均线数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

struct2=FactorsLib2.Factors.MA(5, pricearray);      % 也可直接输入数组求其N日均线，返回的是和输入数组长度相等的数组，但前N-1天数据为NaN

%% 股东总户数，户均持股数
% 函数参数：ShareHolders(因子名，6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间,是否补全自然日数据);
% 是否补全自然日数据：1代表补全，0代表不补全
% 因子名：股东总户数，户均持股数
struct=FactorsLib2.Factors.ShareHolders('股东总户数',{'000001','000002'},727200,736875,1);

value=double(struct.value);             %因子数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

%% 股本信息
% 函数参数：ShareStru(因子名，6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间,是否补全自然日数据);
% 是否补全自然日数据：1代表补全，0代表不补全
% 因子名：总股本,流通A股,流通比例,优先股
struct=FactorsLib2.Factors.ShareStru('总股本',{'000001','000002'},727200,736875,1);

value=double(struct.value);             %因子数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

%% 市值信息
% 函数参数：Capital(因子名，6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间);
% 因子名：总市值,流通市值
struct=FactorsLib2.Factors.Capital('总市值',{'000001','000002'},727200,736875);

value=double(struct.value);             %因子数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

%% 换手率
% 函数参数：TurnoverRate(因子名，6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间);
% 换手率输出日期按自然日序列，当天无交易时数值为NaN
struct=FactorsLib2.Factors.TurnoverRate({'000001','000002'},727200,736875);

value=double(struct.value);             %因子数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

%% 机构持股信息，大股东持股信息
% 函数参数：StockHolding(因子名，6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间,是否补全自然日数据);
% 是否补全自然日数据：1代表补全，0代表不补全
% 因子名：前十大股东持股数量合计,前十大股东持股比例合计,机构持股比例合计,基金持股比例,券商持股比例,QFII持股比例,保险公司持股比例,社保基金持股比例,企业年金持股比例,信托公司持股比例,银行持股比例
struct=FactorsLib2.Factors.StockHolding('前十大股东持股数量合计',{'000001','000002'},727200,736875,1);

value=double(struct.value);             %因子数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

%% 大股东增减持信息
% 函数参数：PositionChange(因子名，6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间);
% 因子名：变动数量,变动数量占流通量比例,最新持有流通数量占流通量比例,平均价格,最新持股总数,买卖方向（减持 0，增持 1）,持有人类型(个人 0，高管 1，公司 2)
struct=FactorsLib2.Factors.PositionChange('买卖方向',{'000001','000002'},727200,736875);

value=double(struct.value);             %因子数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

%% 高管增减持信息
% 函数参数：ShareStru(因子名，6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间);
% 因子名：变动数,变动后持股数,成交均价
struct=FactorsLib2.Factors.LeaderPositionChange('变动数',{'000001','000002'},727200,736875);

value=double(struct.value);             %因子数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

%% 涨跌幅
% 函数参数：PriceChange(涨跌幅周期周期,6位股票代码组成的数组,MATLAB格式开始时间,MATLAB格式结束时间);
% 计算当日收盘价与90天前收盘价对比的涨跌幅,单位为%
% 若不输入股票代码，则输出的是全A非退市股票的涨跌幅
struct=FactorsLib2.Factors.PriceChange(90,{'000001','000002'},730600,736875); % 函数返回90日涨跌幅数据
struct2=FactorsLib2.Factors.PriceChange(90,730600,736875); % 函数返回全A非退市股票90日涨跌幅数据

value=double(struct.value);             %均线数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列


