clc
clear
f = [-7;-5];
A =[3 2
      4 6
      0 7];
b  = [80; 220; 230];
lb = zeros(2,1);
%然后调用linprog函数：
[x,fval,exitflag,output,lambda] = linprog(f,A,b,[],[],lb)
