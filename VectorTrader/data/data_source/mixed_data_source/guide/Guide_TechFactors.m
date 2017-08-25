NET.addAssembly([pwd,'FactorsLib2.dll']);
factors=FactorsLib2.Factors; % 实例化
%重要：技术指标函数在C#中全部为非静态方法，因此必须实例化再引用，不能直接进行引用（直接用FactorsLib2.Factors.MACD会报错）

%% 计算技术指标需先获取行情数据（open,high,low,close,vol），格式为m×n二维矩阵，m为时间序列，n为股票序列
% 例：
    % 求日线MACD指标，先获取行情数据：
    closestruct=FactorsLib2.Factors.DayClose({'000001','000002'},730600,736875,1,-1); close=double(closestruct.value);
    % 再放入MACD函数：(第一个参数表示输出类型，可选：'value','sdo','signal','all',分别表示因子值、无量纲化值、信号值、全部输出。)
    sd=factors.MACD('signal',close);
    % 输出：
        value=double(sd.value); %因子值，3维矩阵，前2维对应输入的close的m×n，第3维长度等于要输出的值的个数（若输出信号值，第3维长度均为1）
        info=cell(sd.info); %因子输入参数及输出值信息

%% 全部36个技术指标函数
sd2=factors.AD('signal',high,low,close,vol);
sd3=factors.CHO('signal',high,low,close,vol);
sd4=factors.ARBR('signal',open,high,low,close);
sd5=factors.ADTM('signal',open,high,low);
sd6=factors.MFI('signal',high,low,close,vol);
sd7=factors.ENV('signal',close);
sd8=factors.EMV('signal',high,low,vol);
sd9=factors.DMI('signal',high,low,close);
sd10=factors.DMA('signal',close);
sd11=factors.DKX('signal',open,high,low,close);
sd12=factors.CR('signal',high,low,close);
sd13=factors.CMO('signal',close);
sd14=factors.BIAS('signal',close);
sd15=factors.MA('signal',close);
sd16=factors.EMA('signal',close);
sd17=factors.MTM('signal',close);
sd18=factors.CCI('signal',high,low,close);
sd19=factors.BOLL('signal',close);
sd20=factors.KDJ('signal',high,low,close);
sd21=factors.MACD('signal',close);
sd22=factors.AMV('signal',open,close,vol);
sd23=factors.SKDJ('signal',high,low,close);
sd24=factors.RVI('signal',close);
sd25=factors.VMA('signal',open,high,low,close);
sd26=factors.VPT('signal',close,vol);
sd27=factors.WVAD('signal',open,high,low,close,vol);
sd28=factors.WMS('signal',open,high,low);
sd29=factors.WAD('signal',open,high,low);
sd30=factors.WMA('signal',close);
sd31=factors.VMACD('signal',vol);
sd32=factors.TRIX('signal',close);
sd33=factors.ROC('signal',close);
sd34=factors.PVI('signal',close,vol);
sd35=factors.PSY('signal',close);
sd36=factors.OSC('signal',close);
sd37=factors.NVI('signal',close,vol);