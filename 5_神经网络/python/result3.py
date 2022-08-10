import numpy as np
import pandas as pd
from numpy import shape
A = []
B = []

data = np.zeros((450, 21))
for i in range(1, 22):
    if i <= 14:
        PATH = 'A'
        b = np.load("npy/" + PATH + str(i)  +  ".npy")
        mut1 = b[250:450, 0] * b[250:450, 1]
        # mut2 = b[350:450, 0] * b[350:450, 1]
        A.append(mut1)
        # print("A", A)
    if i > 14:
        PATH = 'B'
        b = np.load("npy/" + PATH + str(i % 14)  +  ".npy")
        mut2 = b[250:450, 0] * b[250:450, 1]
        B.append(mut2)
        # print("B", B)
A = np.array(A)
B = np.array(B)

dfA = pd.DataFrame(A)
dfB = pd.DataFrame(B)
# print(A)
# dfA.to_csv("./csv/dfA.csv")
# dfB.to_csv("./csv/dfB.csv")
# print(dfA)
for i in range(0, 14):
    print("A<350:" + "  组 ：" + str(i + 1) + "  温度 ：" + str(np.argmax(A[i, 0:100]) + 251) + "   C4烯烃收率： " + str(A[i, np.argmax(A[i, 0:100])]))
    print("A>350:" + "  组 ：" + str(i + 1) + "  温度 ：" + str(np.argmax(A[i, 100:200]) + 351) + "   C4烯烃收率： " + str(A[i, np.argmax(A[i, 100:200])]))

for i in range(0, 7):
    print("B<350:" +  "  组 ：" + str(i + 1) + "  温度 ：" + str(np.argmax(B[i, 0:100]) + 251) + "   C4烯烃收率： " + str(B[i, np.argmax(B[i, 0:100])]))
    print("B>350:" +  "  组 ：" + str(i + 1) + "  温度 ：" + str(np.argmax(B[i, 100:200]) + 351) + "   C4烯烃收率： " + str(B[i, np.argmax(B[i, 100:200])]))

# print(shape(A))
# print(A)