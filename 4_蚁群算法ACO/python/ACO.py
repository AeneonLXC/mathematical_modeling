import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

Ant=100 # 蚂蚁的数量
Times=505 # 蚂蚁的移动次数
Rou=0.9 # 信息数的挥发系数
p0=0.2 # 转移概率常数
Lower_1=-1 # 设置搜索范围
Upper_1=1
Lower_2=-1
Upper_2=1

x = np.zeros((Ant,2))

for i in range(Ant):
    x[i, 0] = (Lower_1 + (Upper_1 - Lower_1) * np.random.randn(1)[0])
    x[i, 1] = (Lower_2 + (Upper_2 - Lower_2) * np.random.randn(1)[0])

step = 0.05

def F(x1, x2):
    """
    函数值的计算

    Parameters
    ----------
    x : TYPE
        蚁群的坐标.

    Returns
    -------
    f : TYPE
        返回函数值.

    """
    # x1 = x[:,0]
    # x2 = x[:,1]
    f = -(x1**4 + x2**4 - np.cos(3*np.pi*x1) - 0.4*np.cos(4*np.pi*x2) + 0.6)
    f = np.reshape(f,(1,-1))#以行的形式输出
    return f

f = F(x[:, 0], x[:, 1])

tau_Best = np.zeros((1,Times))
bestIndex = [0]
p = np.zeros((Times,Ant))
xx = []
for T in range(Times):
    lamda = 1 / (T+1)
    tau_Best[0,T] = np.max(f)
    bestIndex[0] = np.argmax(f) 
    
    for i in range(Ant):
        p[T, i] = (f[0, bestIndex[0]] - f[0,i]) / f[0, bestIndex[0]]
        
    for i in range(Ant):
        if p[T, i] < p0:
            temp1 = x[i, 0] + (2 * np.random.randn(1)[0] - 1) * lamda
            temp2 = x[i, 1] + (2 * np.random.randn(1)[0] - 1) * lamda
        else:
            temp1 = x[i, 0] + (Upper_1 - Lower_1) - (np.random.randn(1)[0] * 0.5)
            temp2 = x[i, 1] + (Upper_2 - Lower_2) - (np.random.randn(1)[0] * 0.5)
        
        if temp1 < Lower_1:
            temp1 = Lower_1
            
        if temp1 > Upper_1:
            temp1 = Upper_1
            
        if temp2 < Lower_2:
            temp2 = Lower_2
            
        if temp2 > Upper_2:
            temp2 = Upper_2
        
        if F(temp1,temp2)[0][0] > F(x[i, 0], x[i, 1])[0][0]:
            # print("temp1: ",temp1)
            # print("temp2: ",temp2)
            x[i, 0] = temp1
            x[i, 1] = temp2
    for i in range(Ant):
        f[0, i] = (1 - Rou) * f[0, i] + F(x[i, 0], x[i, 1])[0][0]
    print(np.max(f))
    
    xx.append(np.max(f))
    plt.plot(xx, lw=3, label='funcotio_max_value_x')
    plt.legend()
    plt.show()
    

