function [xm,fv] = PSO(fitness,N,c1,c2, w,M,D)
% 初始化条件
% c1 学习因子1
% c2 学习因子2
% w  惯性权重
% M  最大迭代次数
% D  搜索空间的维度
% N 初始化群体个体数目
% fitness 为待优化的函数 
%%result%%
%xm 为目标函数取最小值时的自变量
%fv 是目标函数的最小值

%初始化种群的个体
format long

for i=1:N
    for j=1:D
        x(i,j) = randn;% randn产生标准正态分布的随机数 初始化位置
        v(i,j) = randn;% randn产生标准正态分布的随机数 初始化速度
    end
end

%计算粒子的适应度 初始化pi 和 pg
for i=1:N
  p(i)=fitness(x(i,:));
  y(i,:)=x(i,:);
end

pg=x(N,:); %pg 为全局最优
for i=1:(N-1)
    if fitness(x(i,:)) < fitness(pg)
        pg=x(i,:);
    end
end

 %主循环，按照公式依次迭代，直到满足精度要求
 for t=1:M
     for i=1:N %更新速度 位移
         v(i,:)=w*v(i,:) + c1*rand*(y(i,:)-x(i,:))+c2*rand*(pg-x(i,:));
         x(i,:)=x(i,:) + v(i,:);
         if fitness(x(i,:)) < p(i)
             p(i)=fitness(x(i,:));
             y(i,:)=x(i,:);
         end
         if p(i) < fitness(pg)
             pg=y(i,:);
         end
     end
     Pbest(t)=fitness(pg);
 end
 disp("--------xm--------")
 xm=pg
 disp("--------fv--------")
 fv=fitness(pg)
 disp("------------------")