function [newpop]=mutation(pop,pm)
%����
[px,py]=size(pop);
newpop=ones(size(pop));
for i=1:px
    if(rand<pm)
        mpoint=round(rand*py);
        if mpoint<=0%��Ϊ������0-10֮����� ��11�������԰�0��Ϊ1����ֹ����Խ�� 
            mpoint=1
        end
        newpop(i)=pop(i);
        if any(newpop(i,mpoint))==0%any�����ж������Ƿ�Ϊ����Ԫ�� �Ƿ���Ԫ�ط���true��Ϊ1 ����false 0
            newpop(i,mpoint)=1
        else
            newpop(i,mpoint)=0
        end
    else
        newpop(i)=pop(i);
    end
end
            