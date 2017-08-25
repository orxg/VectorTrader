function updatedll
 a=copyfile('\\172.19.62.182\MatlabStrategies\BasicLD','D:\Matlabfiles\LD_dll','f');
 if a==1
     disp('复制成功')
 else
     disp('复制失败')
 end