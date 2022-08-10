
%%main.m
T=1000; %初始化温度值
T_min=1e-12; %设置温度下界
alpha=0.98; %温度的下降率
k=1000; %迭代次数（解空间的大小）
 
x=getX; %随机得到初始解
while(T>T_min)
    for I=1:100
        fx=Fx(x);
        x_new=getX;
        if(x_new>=-2 && x_new<=2)
            fx_new=Fx(x_new);
            delta=fx_new-fx;
            if (delta<0)
                x=x_new+(2*rand-1);
            else
                P=getP(delta,T);
                if(P>rand)
                    x=x_new;
                end
            end
        end
    end
    T=T*alpha;
end
disp('最优解为：')
disp(x)
%%getX.m
function x=getX
    x=4*rand-2;
end
%%Fx.m
function fx=Fx(x)
    fx=(x-2)^2+4;
end
%%getP.m
function p=getP(c,t)
    p=exp(-c/t);
end
