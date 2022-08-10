#分别穷举兵,炮,马,卒,车的各种可能  a,b,c,d,e
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    #每个棋子的取值不同 做判断
                    if a != b and  a != c and a != d and  a != e and \
                    b != c and b != d and b != e and c != d and c != e and d != e:
                        #将竖式计算出来 判断等式是否相等，相等则输出结果
                        m1 = a * 1000 + b * 100 + c * 10 + d
                        m2 = a * 1000 + b * 100 + e * 10 + d
                        s = e * 10000 + d * 1000 + c * 100 + a * 10 + d
                        if s == m1 + m2:
                            print("兵",a)
                            print("炮",b)
                            print("马",c)
                            print("卒",d)
                            print("车",e)
                            
                            
                     