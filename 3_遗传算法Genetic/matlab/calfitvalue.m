function fitvalue=calfitvalue(objvalue)
%计算个体的适应值
%小于0的删除 为了后续概率的计算
 global Cmin;
 Cmin=0;
 [px,py]=size(objvalue);
 for i=1:px
     if objvalue(i)+Cmin>0
         temp=Cmin+objvalue(i);
     else
         temp=0.0;
     end
     fitvalue(i)=temp;
 end
 fitvalue=fitvalue';%不加单引号以列的形式输出 加单引号以行的形式输出