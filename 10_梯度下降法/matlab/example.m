function [k ender]=example(f,x,e)
%�ݶ��½���,fΪĿ�꺯����������x1��x2����xΪ��ʼ��,��[3;4]
syms x1 x2 m; %mΪѧϰ��
d=-[diff(f,x1);diff(f,x2)];  %�ֱ���x1��x2��ƫ���������½��ķ���
flag=1;  %ѭ����־
k=100; %��������
while(flag)
    d_temp=subs(d,x1,x(1));      %����ʼ����룬��õ����½�x1�ݶ�ֵ
    d_temp=subs(d_temp,x2,x(2)); %����ʼ����룬��õ����½�x2�ݶ�ֵ
    nor=norm(d_temp); %����
    if(nor>=e)
        x_temp=x+m*d_temp;            %�ı��ʼ��x��ֵ
        f_temp=subs(f,x1,x_temp(1));  %���ı���x1��x2����Ŀ�꺯��
        f_temp=subs(f_temp,x2,x_temp(2));
        h=diff(f_temp,m);  %��m�󵼣��ҳ����ѧϰ��
        m_temp=solve(h);   %�󷽳̣��õ�����m
        x=x+m_temp*d_temp; %������ʼ��x
        k=k+1;
    else
        flag=0;
    end
end
ender=double(x);  %�յ�
end
