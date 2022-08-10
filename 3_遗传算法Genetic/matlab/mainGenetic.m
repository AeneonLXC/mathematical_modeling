%遗传算法主函数
clear all
popsize=30; %群体大小
chromlength=10;%字符串长度（染色体的长度）
pc=0.7;%交叉概率 
pm=0.005%变异概率
pop=initpop(popsize,chromlength)%随机产生初始群体
epoch=20
for i=1:epoch%epoch为遗传代数
    [objvalue]=calobvalue(pop); %计算目标函数
    fitvalue=calfitvalue(objvalue);%计算群体中每个个体的适应度
    
    %[newpop]=selection(pop,fitvalue);%选择
    [newpop1]=crossover(pop,pc); %交叉
    [newpop2]=mutation(newpop1,pm);  %变异

    [objvalue]=calobvalue(pop); %计算目标函数
    fitvalue=calfitvalue(objvalue);%计算群体中每个个体的适应度
    
    [bestindividual,bestfit]=best(newpop2,fitvalue); %求出群体中适应值最大的个体及其适应值
    y(i)=bestfit; %返回的 y 是自适应度值，而非函数值
    x(i)=decodechrom(bestindividual,1,chromlength)*10/1023; %将自变量解码成十进制
    pop=newpop2;
end

fplot('x+10*sin(5*x)+7*cos(4*x)',[0 10])
hold on
plot(x,y,'r*')                                          
hold on