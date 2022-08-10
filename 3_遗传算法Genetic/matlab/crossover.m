function [newpop]=crossover(pop,pc)
%交叉
[px,py]=size(pop);
newpop=ones(size(pop));%生成和种群一样维度的全一矩阵
for i=1:2:px-1%每隔两个染色体进行一次交叉 px-1防止矩阵越界  
    if(rand<pc)
        cpoint=round(rand*py);
        newpop(i,:)=[pop(i,1:cpoint), pop(i+1,cpoint+1:py)];
        newpop(i+1,:)=[pop(i+1,1:cpoint), pop(i,cpoint+1:py)];
    else
        newpop(i,:)=pop(i);
        newpop(i+1,:)=pop(i+1);
    end
end