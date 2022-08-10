function [newpop]=mutation(pop,pm)
%变异
[px,py]=size(pop);
newpop=ones(size(pop));
for i=1:px
    if(rand<pm)
        mpoint=round(rand*py);
        if mpoint<=0%因为会生成0-10之间的数 有11个，所以把0变为1，防止数组越界 
            mpoint=1
        end
        newpop(i)=pop(i);
        if any(newpop(i,mpoint))==0%any函数判断数组是否为非零元素 是非零元素返回true即为1 否则false 0
            newpop(i,mpoint)=1
        else
            newpop(i,mpoint)=0
        end
    else
        newpop(i)=pop(i);
    end
end
            