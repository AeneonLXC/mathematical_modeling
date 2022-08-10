import time
import numpy as np
 
# 样本数为100条，特征数为二维
def get_data(sample_num=100):
    x1 = np.linspace(0, 9, sample_num)
    x2 = np.linspace(4, 13, sample_num)
    x = np.concatenate(([x1], [x2]), axis=0).T
    y = np.dot(x, np.array([3, 4]).T) 
    return x, y
 
 
# BGD
def bgd(x, y, step_size=0.01, max_iter_count=10000):
    w = np.ones((x.shape[1],))
    x1 = x[:, 0]
    x2 = x[:, 1]
    loss = 10
    iter_count = 0
    while abs(loss) > 0.0001 and iter_count < max_iter_count:
        w[0] -= step_size * \
            np.sum((w[0] * x1 + w[1] * x2 - y) * x1) / x.shape[0]
        w[1] -= step_size * \
            np.sum((w[0] * x1 + w[1] * x2 - y) * x2) / x.shape[0]
        loss = np.sum(w[0] * x1 + w[1] * x2 - y)
        iter_count += 1
        print("iter_count:%d    the loss:%f" % (iter_count, loss))
    return w
 
 
# SGD
def sgd(x, y, step_size=0.01, max_iter_count=10000):
    w = np.ones((x.shape[1],))
    x1 = x[:, 0]
    x2 = x[:, 1]
    loss = 10
    iter_count = 0
    while abs(loss) > 0.00001 and iter_count < max_iter_count:
        i = np.random.randint(x.shape[0])
        w[0] -= step_size * (w[0] * x1[i] + w[1] * x2[i] - y[i]) * x1[i]
        w[1] -= step_size * (w[0] * x1[i] + w[1] * x2[i] - y[i]) * x2[i]
        loss = np.sum(w[0] * x1 + w[1] * x2 - y)
        iter_count += 1
        print("iter_count:%d    the loss:%f" % (iter_count, loss))
    return w
 
# MBGD
def msgd(x, y, batch_size, step_size=0.01, max_iter_count=10000):
    w = np.ones((x.shape[1],))
    x1 = x[:, 0]
    x2 = x[:, 1]
    loss = 10
    iter_count = 0
    while abs(loss) > 0.00001 and iter_count < max_iter_count:
        i = np.random.randint(x.shape[0], size=batch_size)
        w[0] -= step_size * \
            np.sum((w[0] * x1[i] + w[1] * x2[i] - y[i]) * x1[i]) / batch_size
        w[1] -= step_size * \
            np.sum((w[0] * x1[i] + w[1] * x2[i] - y[i]) * x2[i]) / batch_size
        loss = np.sum(w[0] * x1 + w[1] * x2 - y)
        iter_count += 1
        print("iter_count:%d    the loss:%f" % (iter_count, loss))
    return w
 
 
if __name__ == '__main__':
    time1 = time.time()
    x, y = get_data()
#     print(bgd(x, y))
#     print(sgd(x, y))
    print(msgd(x, y, 10))
    time2 = time.time()
    print(time2 - time1)