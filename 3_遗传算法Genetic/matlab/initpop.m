function pop=initpop(popsize,chromlength)
%--- �������� ---%
%initpop ��ʵ��Ⱥ��ĳ�ʼ��%
%chromlenth��ʾȾɫ��ĳ��ȣ���ֵ���ĳ��ȣ��� ���ȵĴ�Сȡ���ڱ����Ķ����Ʊ���ĳ���               %
pop=round(rand(popsize,chromlength));
% rand �������ÿ����ԪΪ��0��1��������Ϊpopsize������Ϊchromlenth�ľ���
%round ���������뺯��
end