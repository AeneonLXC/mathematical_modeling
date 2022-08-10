import = table2array(adjust1);%将表格数据转化为数组
trian = import(:,1:18);%划分训练集
test = import(:,18:26);%划分真实数据集
