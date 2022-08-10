function [objvalue]=calobjvalue(pop)
%实现目标函数的计算
temp1=decodechrom(pop,1,10);% 将pop每行转化为十进制数
x=temp1*10/1023;% 将二值域中的数转化为变量域中的数
objvalue=9*sin(5*x)+7*cos(4*x);
end