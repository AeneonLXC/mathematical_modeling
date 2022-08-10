import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from numpy import shape
from tensorflow import keras
import pandas as pd
import copy
path = "C:/Users/23608/Desktop/2.csv"

# path = 'C:/Users/lyh/Desktop/coding/B/1.csv'

data = np.loadtxt(path, dtype="double", delimiter=',', skiprows=0, usecols=None, unpack=False)
idx = [0]
for i in range(data.shape[0] - 1):
    if data[i, 0] > data[i + 1, 0]:
        idx.append(i + 1)
idx.append(i + 1)
data_imp = np.zeros((data.shape[0], 5))

# df = pd.DataFrame(data)
# df.to_csv("./csv/data.csv")

# data_imp[:, 4] = data[:, 0] / 100
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

input = np.array(data_imp)
out = np.array(data_out)

print(shape(data_imp))
print(shape(data_out))

from sklearn import tree

model_decision_tree_regression = tree.DecisionTreeRegressor()

# 2.线性回归
from sklearn.linear_model import LinearRegression

model_linear_regression = LinearRegression()

# 3.SVM回归
from sklearn import svm

model_svm = svm.SVR()

# 4.kNN回归
from sklearn import neighbors

model_k_neighbor = neighbors.KNeighborsRegressor()

# 5.随机森林回归
from sklearn import ensemble

model_random_forest_regressor = ensemble.RandomForestRegressor(n_estimators=20)  # 使用20个决策树

# 6.Adaboost回归
from sklearn import ensemble

model_adaboost_regressor = ensemble.AdaBoostRegressor(n_estimators=50)  # 这里使用50个决策树

# 7.GBRT回归
from sklearn import ensemble

model_gradient_boosting_regressor = ensemble.GradientBoostingRegressor(n_estimators=100)  # 这里使用100个决策树

# 8.Bagging回归
from sklearn import ensemble

model_bagging_regressor = ensemble.BaggingRegressor()

# 9.ExtraTree极端随机数回归
from sklearn.tree import ExtraTreeRegressor

model_extra_tree_regressor = ExtraTreeRegressor()

from sklearn.linear_model import ElasticNet
modelElasticNet = ElasticNet(random_state=0)


from sklearn.neural_network import MLPClassifier
etworkMLPClassifier = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)


from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

model_bagging_regressor.fit(input, out)

result = model_bagging_regressor.predict(input)
loss = result - out

# import pydotplus
# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf("iris.pdf")
# from sklearn import tree
# import pydotplus
# import os
# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
# dot_data = tree.export_graphviz(clf, out_file=None,
#                          feature_names=["sepal length","sepal width"],
#                          class_names=iris.target_names,
#                          filled=True, rounded=True,
#                          special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data)
# Image(graph.create_png())
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()


clsf=clf.fit(input,out.astype('int'))

# tree.plot_tree(clsf)
plt.figure(1)
plt.title("bagging")
plt.xlabel("x")
plt.ylabel("y")
plt.bar(np.arange(len(result)), loss[:,0],label="CH3CH2OH")
plt.bar(np.arange(len(result)), loss[:,1], label="C4=")
plt.figure(2)


# plt.figure(3)
# plt.plot(np.arange(len(result)), out[:, 0], label="CH3CH2OH")
# plt.plot(np.arange(len(result)), out[:, 1], label="C4=")
# plt.savefig("./img/sklearn-forest.jpg")

# plt.plot(np.arange(len(result)), result, "ro-", label="Predict value")
# plt.title(f"method:{method}---score:{score}")
plt.legend(loc="best")
plt.show()























