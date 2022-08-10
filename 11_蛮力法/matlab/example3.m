count=1
for i = 1:1000
    for j = 1:1000
        x=i/100;
        y=j/100;
        if x+y <= 4 && x + 3*y <=6
            dictr(count)=3*x+5*y;
            count = count + 1;
        end
    end
end
plot(dictr(1:100:count),"-r*");
title("目标函数曲线")
            
        