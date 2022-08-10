import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import copy
import datetime
path = "./csv/2.csv"

data = np.loadtxt(path, dtype="double", delimiter=',', skiprows=0, usecols=None, unpack=False)
idx = [0]
for i in range(data.shape[0] - 1):
    if data[i, 0] > data[i + 1, 0]:
        idx.append(i + 1)
idx.append(i + 1)
data_imp = np.zeros((data.shape[0], 5))

data_imp[:, 4] = data[:, 0]
data_imp[0:5, 0] = 200
data_imp[0:5, 1] = 1
data_imp[0:5, 2] = 200
data_imp[0:5, 3] = 1.68
data_imp[5:10, 0] = 200
data_imp[5:10, 1] = 2
data_imp[5:10, 2] = 200
data_imp[5:10, 3] = 1.68
data_imp[10:17, 0] = 200
data_imp[10:17, 1] = 1
data_imp[10:17, 2] = 200
data_imp[10:17, 3] = 0.9
data_imp[17:23, 0] = 200
data_imp[17:23, 1] = 0.5
data_imp[17:23, 2] = 200
data_imp[17:23, 3] = 1.68
data_imp[23:29, 0] = 200
data_imp[23:29, 1] = 2
data_imp[23:29, 2] = 200
data_imp[23:29, 3] = 0.3
data_imp[29:34, 0] = 200
data_imp[29:34, 1] = 5
data_imp[29:34, 2] = 200
data_imp[29:34, 3] = 1.68
data_imp[34:39, 0] = 50
data_imp[34:39, 1] = 1
data_imp[34:39, 2] = 50
data_imp[34:39, 3] = 0.3
data_imp[39:44, 0] = 50
data_imp[39:44, 1] = 1
data_imp[39:44, 2] = 50
data_imp[39:44, 3] = 0.9
data_imp[44:49, 0] = 500
data_imp[44:49, 1] = 1
data_imp[44:49, 2] = 50
data_imp[44:49, 3] = 2.1
data_imp[49:54, 0] = 50
data_imp[49:54, 1] = 5
data_imp[49:54, 2] = 50
data_imp[49:54, 3] = 2.1
data_imp[54:59, 0] = 50
data_imp[54:59, 1] = 1
data_imp[54:59, 2] = 90
data_imp[54:59, 3] = 1.68
data_imp[59:64, 0] = 50
data_imp[59:64, 1] = 1
data_imp[59:64, 2] = 50
data_imp[59:64, 3] = 1.68
data_imp[64:69, 0] = 67
data_imp[64:69, 1] = 1
data_imp[64:69, 2] = 33
data_imp[64:69, 3] = 1.68
data_imp[69:74, 0] = 33
data_imp[69:74, 1] = 1
data_imp[69:74, 2] = 67
data_imp[69:74, 3] = 1.68
data_imp[74:79, 0] = 50
data_imp[74:79, 1] = 1
data_imp[74:79, 2] = 50
data_imp[74:79, 3] = 1.68
data_imp[79:84, 0] = 100
data_imp[79:84, 1] = 1
data_imp[79:84, 2] = 100
data_imp[79:84, 3] = 1.68
data_imp[84:90, 0] = 10
data_imp[84:90, 1] = 1
data_imp[84:90, 2] = 10
data_imp[84:90, 3] = 1.68
data_imp[90:96, 0] = 25
data_imp[90:96, 1] = 1
data_imp[90:96, 2] = 25
data_imp[90:96, 3] = 1.68
data_imp[96:102, 0] = 50
data_imp[96:102, 1] = 1
data_imp[96:102, 2] = 50
data_imp[96:102, 3] = 2.1
data_imp[102:108, 0] = 75
data_imp[102:108, 1] = 1
data_imp[102:108, 2] = 75
data_imp[102:108, 3] = 1.68
data_imp[108:114, 0] = 100
data_imp[108:114, 1] = 1
data_imp[108:114, 2] = 100
data_imp[108:114, 3] = 0.9
data_out = data[:, [1, 3]]
summary_writer = tf.summary.create_file_writer('./chem/torb')
def mod():
    model = tf.keras.Sequential()
    model.add(keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Dense(units=150,
                                    activation=tf.keras.activations.relu))
    model.add(keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Dense(units=100,
                                    activation=tf.keras.activations.relu))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.AlphaDropout(rate=0.5))
    model.add(tf.keras.layers.Dense(units=2,
                                    activation=tf.keras.activations.relu))
    return model
tf.summary.trace_on(graph=True, profiler=True)
train_loss = tf.keras.metrics.Mean('input_loss', dtype=tf.float32)

opt = tf.keras.optimizers.Adam(lr=0.0001)
modd = mod()
losslist = []
for i in range(1000):
    with tf.GradientTape(persistent=True) as tape:
        out = modd(data_imp)
        loss = tf.reduce_mean(tf.sqrt(tf.square(out - data_out) + 0.00001))  # 均方误差
        loss_regularization = []
    train_loss(loss)
    grad = tape.gradient(loss, modd.trainable_variables)
    opt.apply_gradients(zip(grad, modd.trainable_variables))
    if i % 20 == 0:
        print(loss)
    losslist.append(loss)
data_test = np.zeros((450, 5))
x = [250, 450]
for i in range(x[0], x[1]):
    data_test[i, 0:4] = np.array(([200, 1, 200, 1.68]))
    data_test[i, 4] = i

for i in range(x[0], x[1]):
    data_test[i, 0:4] = np.array(([100, 1, 100, 1.68]))
    data_test[i, 4] = i


out = modd(data_test)
print(out)
# print(out[250:450, 0])
modd.summary()
if __name__ == '__main__':
    outcopy = np.array(copy.deepcopy(out))
    plt.plot(out[x[0]:x[1], 0], lw=3, label='CH3CH2OH')
    plt.plot(out[x[0]:x[1], 1], lw=3, label='C4=')
    plt.xlabel('tem')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    plt.title("LOSS")
    plt.xlabel("LOSS-x")
    plt.ylabel("LOSS-y")
    plt.plot(losslist, lw=3, label='LOSS')
    plt.legend()
    # plt.savefig("./img/Group-B.jpg")
    plt.show()
