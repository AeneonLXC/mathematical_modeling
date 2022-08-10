import numpy as np
import matplotlib.pyplot as plt
def f(x1, x2):
    #目标函数
    return np.square((x1 - 5)) + np.square((x2 - 7))
#生成一组等差数列，范围0-10，个数100个
x1 = np.linspace(0,10,100)
x2 = np.linspace(0,10,100)

l = []
xx = []
#迭代开始
for i in range(x1.shape[0]):
    for j in range(x2.shape[0]):
        y = f(x1[i],x2[j])
        xx.append(y)
        l.append([y,x1[i],x2[j]])
plt.plot(xx[::100], lw=3, label='l')
plt.legend()
plt.show()
l = np.array(l)
print("最小值为：", np.min(l[:,0]))
print("x1的取值为：", l[np.argmin(l[:,0]),1])
print("x2的取值为：", l[np.argmin(l[:,0]),2])




