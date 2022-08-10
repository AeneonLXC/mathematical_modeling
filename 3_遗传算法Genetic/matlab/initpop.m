function pop=initpop(popsize,chromlength)
%--- 函数介绍 ---%
%initpop 是实现群体的初始化%
%chromlenth表示染色体的长度（二值数的长度）， 长度的大小取决于变量的二进制编码的长度               %
pop=round(rand(popsize,chromlength));
% rand 随机产生每个单元为（0，1），行数为popsize，列数为chromlenth的矩阵
%round 是四舍五入函数
end