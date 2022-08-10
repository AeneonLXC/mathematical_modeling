function [min,path] = dijkstra(w,start,terminal)
n = size(w,1); %��ȡ���ڽӾ������ Ҳ��ʾ�м������
label(start) = 0; %��ʼ��l
f(start) = start; %��ʼ��f
%�������н�㣬������ʼ���֮��ĵ����inf
for i = 1:n
    if i~= start
        label(i) = inf;
    end
end
%��ʼ��s���ϣ�u���
s(1) = start;
u  = start;
%ѭ������
while length(s) < n
    for i = 1:n
        ins = 0;%insΪ��¼ֵ
        for j = 1:length(s)
            if i == s(j)%���Ѿ������ý�㣬��pass
                ins = 1;
            end
        end
        if ins == 0%��δ�����ǽ��
            v = i; %��¼�ý��
            if label(v) > (label(u) + w(u,v))%�����n->v�ľ��� ���ڽ��n->u�ľ��� ���� u->v�ľ���
                label(v) = (label(u) + w(u,v));%����l
                f(v) = u;%����f
            end
        end
    end

min = label(terminal);%����С�ľ����¼
path(1) = terminal;%��¼·��
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
    
