import numpy as np
import matplotlib.pyplot as plt

def E(x, y):
    """
    目标函数  x的取值范围为 -5 < x < 5
    
    Parameters
    ----------
    x : 实数
        x1的值.
    y : 实数
        x2的值.

    Returns
    -------
    res : 实数
        返回目标函数值.

    """
    res= 4*x**2-2.1*x**4+(x**6)/3+x*y-4*y**2+4*y**4
    return res

def randValue(t, x, y):
    """
    扰乱生成x1，x2的值
    
    Parameters
    ----------
    t : 实数
        当前的温度.
    x : 实数
        x1的值.
    y : 实数
        x2的值.

    Returns
    -------
    x_ : 实数
        x1的新值.
    y_ : 实数
        x2的新值.

    """
    while 1:
        x_ = x + t * (np.random.rand(1)[0] - np.random.rand(1)[0])
        y_ = y + t * (np.random.rand(1)[0] - np.random.rand(1)[0])
        if x_ >= -5 and x_ <= 5 and y_ >= -5 and y_ <= 5:
            break
    return x_, y_

def select(t ,e, e_):
    """
    是否进行下降法则

    Parameters
    ----------
    t : 实数
        当前温度.
    e : 实数
        当前函数值.
    e_ :实数
        新的函数值.

    Returns
    -------
    int
        是否选择 选择为1 拒绝为0.

    """
    if e_ <= e:
        return 1
    else:
        p = np.power(np.e, -(e_ - e) / t)
        if p > np.random.rand(1)[0]:
            return 1
        else:
            return 0
        
if __name__ == "__main__":      
    t0 = 100 # 初始温度
    t = t0 # 当前温度 
    alpha = 0.99 # 降温系数
    tf = 0.01 #最终温度
    xx = []
    x = (np.random.rand(1,100) * 10) - 4  # 随机生成一组解 为-6 到 6 可以取到 5
    y = (np.random.rand(1,100) * 10) - 4  # 随机生成一组解 为-6 到 6 可以取到 5
    
    while t > tf:
        for i in range(t0):
            e = E(x[0, i], y[0, i])
            x_, y_ = randValue(t, x[0, i], y[0, i])
            e_ = E(x_, y_)
            if select(t, e, e_):
                x[0, i] = x_
                y[0, i] = y_
        e_result = E(x, y)
        e_best = np.min(e_result)
        e_inx = np.argmin(e_result)
        xx.append(e_best)
        x_value = x[0, e_inx]
        y_value = y[0, e_inx]
        
        t = t * alpha 
        print("e_best", e_best)
        print("x_value", x_value)
        print("y_value", y_value)
        
plt.plot(xx, lw=3, label='e_best')
plt.legend()
plt.show()
