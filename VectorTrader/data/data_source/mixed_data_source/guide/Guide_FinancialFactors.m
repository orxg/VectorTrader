NET.addAssembly([pwd,'FactorsLib2.dll']);

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
struct=FactorsLib2.Factors.Capital('流通市值',{'000001','000002'},727200,736875);

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
struct2=FactorsLib2.Factors.PriceChange(90,730600,736875,15); % 函数返回全A非退市且未连续停牌超15天的股票90日的涨跌幅数据（最后一个参数若省略，即不剔除连续停牌股票）

value=double(struct.value);             %均线数据，行按照numtime排列，列按照stockcode排列
numtime=single(struct.numtime)';        %时间序列
stockcode=cell(struct.stockcode)';      %股票代码序列
market=cell(struct.market)';            %市场代码序列

%% 资产负债率
% 函数参数：AssetToLiabilityRatio(股票代码组成的cell,开始时间,结束时间);
struct=FactorsLib2.Factors.AssetToLiabilityRatio({'000001','000002'},727200,736875);

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