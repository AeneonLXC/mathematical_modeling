import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
def fitness(x):
    F = 0
    for i in range(x.shape[0]):
        F = F + x[i]**2 + x[i] - 6
    return F

def PSO(N,c1,c2,w,M,D):
    """
    初始化条件
    Parameters
    ----------
    fitness : TYPE
        目标函数
    N : TYPE
        初始化群体个体数目
    c1 : TYPE
        学习因子1
    c2 : TYPE
        学习因子2
    w : TYPE
        惯性权重
    M : TYPE
        最大迭代次数
    D : TYPE
        搜索空间的维度
    Returns
    -------
    xm 为目标函数取最小值时的自变量
    fv 是目标函数的最小值

    """
    img = np.zeros((600,600,3))
    
    x = np.zeros((N,D))
    y = np.zeros((N,D))
    v = np.zeros((N,D))
    p = {}
    p_best = {}
    for i in range(N):
        for j in range(D):
            x[i,j] = np.random.randn(1)[0] #初始化位置
            v[i,j] = np.random.randn(1)[0] #初始化速度
    # 计算粒子的适应度 初始化pi 和 pg
    for i in range(N):
        p[i] = fitness(x[i,:])
        y[i,:] = x[i,:]
        
    pg = x[N-1,:]
    
    fv_lidt = []
    
    for i in range(N-1):
        if fitness(x[i,:]) < fitness(pg):
            pg = x[i, :]
    
    for t in range(M):
        for i in range(N):
            v[i,:] = w*v[i,:] + c1*np.random.rand(1)[0]*(y[i,:] - x[i,:])+c2*np.random.rand(1)[0]*(pg-x[i,:])
            x[i,:] = x[i,:] + v[i,:]
            
            fv_lidt.append(fitness(x[i,:]))
            if fitness(x[i,:]) < p[i]:
                p[i] = fitness(x[i,:])
                y[i, :] = x[i, :]
            if p[i] < fitness(pg):
                pg = y[i,:]

        p_best[t]=fitness(pg)
        
    xm = pg
    fv = fitness(pg)
    
    print("xm: ", pg)
    print("fv: ", fitness(pg))
        
    return xm, fv_lidt

if __name__ == "__main__":
    N = 50
    c1 = 1.5
    c2 = 2.5
    w = 0.5
    M = 10
    D = 30                              
    x1 = np.zeros((1,30))
    xm1,fv2 = PSO(N, c1, c2, w, M, D)
    
    plt.plot(xm1, lw=3, label='xm1')
    plt.legend()
    plt.show()
    
    plt.plot(fv2, lw=3, label='fv2')
    plt.legend()
    plt.show()