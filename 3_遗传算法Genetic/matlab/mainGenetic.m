%�Ŵ��㷨������
clear all
popsize=30; %Ⱥ���С
chromlength=10;%�ַ������ȣ�Ⱦɫ��ĳ��ȣ�
pc=0.7;%������� 
pm=0.005%�������
pop=initpop(popsize,chromlength)%���������ʼȺ��
epoch=20
for i=1:epoch%epochΪ�Ŵ�����
    [objvalue]=calobvalue(pop); %����Ŀ�꺯��
    fitvalue=calfitvalue(objvalue);%����Ⱥ����ÿ���������Ӧ��
    
    %[newpop]=selection(pop,fitvalue);%ѡ��
    [newpop1]=crossover(pop,pc); %����
    [newpop2]=mutation(newpop1,pm);  %����

    [objvalue]=calobvalue(pop); %����Ŀ�꺯��
    fitvalue=calfitvalue(objvalue);%����Ⱥ����ÿ���������Ӧ��
    
    [bestindividual,bestfit]=best(newpop2,fitvalue); %���Ⱥ������Ӧֵ���ĸ��弰����Ӧֵ
    y(i)=bestfit; %���ص� y ������Ӧ��ֵ�����Ǻ���ֵ
    x(i)=decodechrom(bestindividual,1,chromlength)*10/1023; %���Ա��������ʮ����
    pop=newpop2;
end

fplot('x+10*sin(5*x)+7*cos(4*x)',[0 10])
hold on
plot(x,y,'r*')                                          
hold on