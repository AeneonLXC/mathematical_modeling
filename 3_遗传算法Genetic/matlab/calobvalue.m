function [objvalue]=calobjvalue(pop)
%ʵ��Ŀ�꺯���ļ���
temp1=decodechrom(pop,1,10);% ��popÿ��ת��Ϊʮ������
x=temp1*10/1023;% ����ֵ���е���ת��Ϊ�������е���
objvalue=9*sin(5*x)+7*cos(4*x);
end