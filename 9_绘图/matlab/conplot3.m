clear
clc
subplot(2,2,1)
contour3(peaks,50); %�������������ȿռ��еĵȸ���
title("���ȿռ��еĵȸ���")
axis([-inf inf -inf inf -inf inf]); 
subplot(2,2,2)
contour(peaks, 50); %��������ȸ�����XYƽ���ͶӰ
title("�ȸ�����XYƽ���ͶӰ")
subplot(2,2,3)
t=linspace(0,20*pi, 501); 
plot3(t.*sin(t), t.*cos(t), t);% �������ȿռ��е�����
title("���ȿռ��е�����")
subplot(2,2,4)
plot3(t.*sin(t), t.*cos(t), t, t.*sin(t), t.*cos(t), -t);% ͬʱ�����������ȿռ��е�����
title("�������ȿռ��е�����")