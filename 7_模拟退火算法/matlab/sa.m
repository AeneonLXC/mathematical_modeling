
%%main.m
T=1000; %��ʼ���¶�ֵ
T_min=1e-12; %�����¶��½�
alpha=0.98; %�¶ȵ��½���
k=1000; %������������ռ�Ĵ�С��
 
x=getX; %����õ���ʼ��
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
disp('���Ž�Ϊ��')
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
