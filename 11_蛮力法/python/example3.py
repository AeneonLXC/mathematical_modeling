import numpy as np
import matplotlib.pyplot as plt
#初始化 x,y的取值
x = 0
y = 0
result = []
epoch = 1000
#目标函数
def f(x,y):
    return 3 * x + 5 * y
#开始迭代
for i in range(epoch):
    for j in range(epoch):
        x,y = i/100,j/100
        #约束条件
        if x + y <= 4 and x + 3 * y <= 6:
            result.append([f(x,y),x,y])

result = np.array(result)
plt.plot(result[:,0], lw=3, label='max value')
plt.plot(result[:,1], lw=3, label='x value')
plt.plot(result[:,2], lw=3, label='y value')
plt.legend()
plt.show()
print("最大值为：",np.max(result[:,0]))
print("x的值为：",result[np.argmax(result[:,0]),1])
print("y的值为：",result[np.argmax(result[:,0]),2])



