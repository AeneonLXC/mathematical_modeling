function [newpop]=selection(pop,fitvalue)
totalfit=sum(fitvalue);%����Ӧ��ֵ֮��
fitvalue_pro=fitvalue/(totalfit+0.00001);%�������屻ѡ�еĸ���
fitvalue_pro_cumnsum=cumsum(fitvalue_pro); %�ۼӺ��� [1,2,3,4]->[1,3,6,10]
[px,py]=size(pop);
ms=sort(rand(px,1));%С��������
fitin=1;
newin=1;
while newin<=px
    if(ms(newin))<fitvalue_pro_cumnsum(fitin)
        newpop(newin,:)=pop(fitin,:);
        newin=newin+1;
    else
        fitin=fitin+1;
    end
end
