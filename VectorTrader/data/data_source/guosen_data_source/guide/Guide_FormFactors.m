NET.addAssembly([pwd,'FactorsLib2.dll']);
factors=FactorsLib2.Factors; % 实例化
%重要：形态指标函数在C#中全部为非静态方法，因此必须实例化再引用，不能直接进行引用

%% 计算形态指标需输入行情数据（open,high,low,close,vol），格式为m×n二维矩阵，m为时间序列，n为股票序列
% 建议输入类型：
sharestruct=FactorsLib2.Factors.ShareStru('流通A股',scc,startdate,enddate,1); % 可输出按自然日补全的流通股本
share=double(sharestruct.value);
closestruct=FactorsLib2.Factors.DayClose(scc,startdate,enddate,-2,-1); % 可输出按自然日但不补全的日线数据
close=double(closestruct.value);

%% 全部形态指标函数
data=double(factors.JinZhenTanDi(open,low,close)); % 金针探底
data=double(factors.KongZhongJiaYou(open,low,close)); % 空中加油
data=double(factors.XiangTiTuPo(high,low,close)); % 箱体突破
data=double(factors.YiYangSiXian(high,low,close)); % 一阳四线
data=double(factors.QingTingDianShui(low,close)); % 蜻蜓点水
data=double(factors.DuoFangPao(open,high,low,close)); % 多方炮
data=double(factors.HongSanBing(open,close)); % 红三兵
data=double(factors.YangBaoYin(open,close)); % 阳包阴
data=double(factors.FangLiangTuPo(high,vol,share)); % 放量突破
% 输出二维m×n矩阵