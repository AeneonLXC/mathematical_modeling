function fitvalue=calfitvalue(objvalue)
%����������Ӧֵ
%С��0��ɾ�� Ϊ�˺������ʵļ���
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
 fitvalue=fitvalue';%���ӵ��������е���ʽ��� �ӵ��������е���ʽ���