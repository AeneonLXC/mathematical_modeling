x1 = linspace(0,10,100);
x2 = linspace(0,10,100);
count=1
for i=1:100
    for j=1:100
        y = f(x1(i),x2(j));
        distr(count) = y;
        count = count + 1;
    end
end
plot(distr(1:100:10000),"*")
title("目标函数曲线")
