NET.addAssembly([pwd,'FactorsLib2.dll']);

%% 获取全部合约，获取市场代码，股票名称
ccode=cell(FactorsLib2.FutureData.getCode()); %获取历史全部合约代码
ccode=cell(FactorsLib2.FutureData.getCode(1)); %获取处于交易状态合约代码
cmarket=cell(FactorsLib2.FutureData.getMarket(ccode)); %获取输入合约的交易所代码（CFFEX-中国金融期货交易所, CZCE-郑州商品交易所, DCE-大连商品交易所, SHFE-上海期货交易所）
cname=cell(FactorsLib2.FutureData.getName(scode)); %获取输入合约的简称
sccode=cell(FactorsLib2.FutureData.getStandardContractCode(N,startdate,enddate)); %获取输入合约的标准合约代码
listedprice=double(FactorsLib2.FutureData.getListedPrice(codes));%获取输入合约的挂牌基准价
dateinfo=cell(FactorsLib2.FutureData.getDateInfo(codes));%获取输入合约的日期信息(默认输出 ‘开始交易日,最后交易日,最后交割日’)
dateinfo=cell(FactorsLib2.FutureData.getDateInfo(codes,'最后交割日'));%获取输入合约的日期信息
dateinfo=cell(FactorsLib2.FutureData.getDateInfo(codes,'开始交易日,最后交易日'));%获取输入合约的日期信息