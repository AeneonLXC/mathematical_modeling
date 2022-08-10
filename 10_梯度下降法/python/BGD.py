#导入依赖包
import numpy as np
import matplotlib.pyplot as plt
#初始化样本集
sample_num=100
x1 = np.linspace(0, 9, sample_num)
x2 = np.linspace(4, 13, sample_num)
x = np.concatenate(([x1], [x2]), axis=0).T
y = np.dot(x, np.array([3, 4]).T)

#初始化权值
w = np.ones((x.shape[1],))

x_1 = x[:, 0]
x_2 = x[:, 1]

#设定步长，迭代次数，循环次数
loss = 10
iter_count = 0
max_iter_count=500                 
step_size=0.01
loos = []

#迭代更新
while abs(loss) > 0.0001 and iter_count < max_iter_count:
    w[0] -= step_size * np.sum((w[0] * x1 + w[1] * x2 - y) * x1) / x.shape[0]
    w[1] -= step_size * np.sum((w[0] * x1 + w[1] * x2 - y) * x2) / x.shape[0]
    loss = np.sum(w[0] * x1 + w[1] * x2 - y)
    iter_count += 1
    print("iter_count:%d    the loss:%f" % (iter_count, loss))
    
    loos.append(abs(loss))
    plt.plot(loos, lw=3, label='loss')
    plt.legend()
    plt.show()
    
    # plt.plot(fv2, lw=3, label='fv2')
    # plt.legend()
    # plt.show()
        
    

    