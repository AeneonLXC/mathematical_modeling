function [min,path] = dijkstra(w,start,terminal)
n = size(w,1); %获取到邻接矩阵的行 也表示有几个结点
label(start) = 0; %初始化l
f(start) = start; %初始化f
%遍历所有结点，将除初始结点之外的点插入inf
for i = 1:n
    if i~= start
        label(i) = inf;
    end
end
%初始化s集合，u结点
s(1) = start;
u  = start;
%循环遍历
while length(s) < n
    for i = 1:n
        ins = 0;%ins为记录值
        for j = 1:length(s)
            if i == s(j)%若已经经过该结点，则pass
                ins = 1;
            end
        end
        if ins == 0%若未经过盖结点
            v = i; %记录该结点
            if label(v) > (label(u) + w(u,v))%若结点n->v的距离 大于结点n->u的距离 加上 u->v的距离
                label(v) = (label(u) + w(u,v));%更新l
                f(v) = u;%更新f
            end
        end
    end

min = label(terminal);%将最小的距离记录
path(1) = terminal;%记录路径
i = 1;

while path(i) ~= start
    path(i+1) = f(path(i));
    i = i + 1;
end

path(i) = start;
L = length(path);
path = path(L:-1:1)

v1 = 0;
k = inf;
for i = 1:n
    ins = 0;
    for j = 1:length(s)
        if i == s(j)
            ins = 1;
        end
    end
    if ins == 0
        v = i;
        if k > label(v)
            k = label(v);
            v1 = v;
        end
    end
end

s(length(s) + 1) = v1;
u = v1;

end
    
