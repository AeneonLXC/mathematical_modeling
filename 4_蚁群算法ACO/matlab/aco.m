clear all
%初始化
Ant=300; % 蚂蚁的数量
Times=800; % 蚂蚁的移动次数
Rou=0.9; % 信息数的挥发系数
p0=0.2; % 转移概率常数
Lower_1=-1; % 设置搜索范围
Upper_1=1;
Lower_2=-1;
Upper_2=1;
for i=1:Ant
    X(i,1)=(Lower_1 + (Upper_1-Lower_1)*rand); % 设置随机位置
    X(i,2)=(Lower_2 + (Upper_2-Lower_2)*rand); % 设置随机位置
    Tau(i)=F(X(i,1),X(i,2)); % 计算目标函数值
end
step=0.05;
f='-(x.^4+3*y.^4-0.2*cos(3*pi*x)-0.4*cos(4*pi*y)+0.6)';

[x,y]=meshgrid(Lower_1:step:Upper_1, Lower_2:step:Upper_2);
z=eval(f); % z轴
figure(1);
subplot(1,2,1);
mesh(x,y,z); % 得到一个蜘蛛网
hold on;
plot3(X(:,1),X(:,2),Tau,"k*") % 绘制三维图
hold on;
text(0.1,0.8,1,"蚂蚁的初始位置");
xlabel("x");
ylabel("y");
zlabel("f(x,y)");
for T=1:Times
    lamda=1/T;
    [Tau_Best(T),BestIndex]=max(Tau); % 返回函数的最大值和其索引
    for i=1:Ant
        P(T,i)=(Tau(BestIndex)-Tau(i)) / Tau(BestIndex); % 计算状态转移概率
    end
    for i=1:Ant
        if P(T,i)<p0 % 局部搜索
            temp1=X(i,1)+(2*rand-1)*lamda;
            temp2=X(i,2)+(2*rand-1)*lamda;
        else
            temp1=X(i,1)+(Upper_1-Lower_1)-(rand*0.5);
            temp2=X(i,2)+(Upper_2-Lower_2)-(rand*0.5);
        end
        % 越界处理 
        if temp1<Lower_1
            temp1=Lower_1;
        end
        if temp1>Upper_1
            temp1=Upper_1;
        end
        if temp2<Lower_2
            temp2=Lower_2;
        end
        if temp2>Upper_2
            temp2=Upper_2;
        end
        if F(temp1,temp2)>F(X(i,1),X(i,2)) % 判断蚂蚁是否移动
            X(i,1)=temp1;
            X(i,2)=temp1;
        end
    end
    for i=1:Ant
        Tau(i)=(1-Rou)*Tau(i)+F(X(i,1),X(i,2));
    end
end
subplot(1,2,2);
mesh(x,y,z);
hold on;
x = X(:,1);
y = X(:,2);
plot3(x,y,eval(f),"k*"); % 绘制三维图
hold on;
text(0.1,0.8,1,"蚂蚁的最终分布位置");
xlabel("x");
ylabel("y");
zlabel("f(x,y)");
