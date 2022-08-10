import pandas as pd
import numpy as np
import copy as cp
import matplotlib.pyplot as plt

path = "./csv/附件1.xlsx"
df = pd.read_excel(path)
x_data = np.array(df[["温度", "乙醇转化率(%)", "C4烯烃选择性(%)"]])
result = np.zeros((len(x_data[:, -1]), 4))
x1 = []
x2 = []
x3 = []


def numberMethod(xarray, df):
    x_ken = cp.deepcopy(xarray)
    x_head = cp.deepcopy(df)
    temp1 = 0
    for i in range(len(x_ken[:121, :]) - 1):
        temp = 0
        if type(x_head["催化剂组合编号"][i]) == str:
            x1.append(i)
    for i in range(1, len(x1)):
        x2.append(x_ken[x1[i - 1]: x1[i], 1])
        x3.append(x_ken[x1[i - 1]: x1[i], 2])


def sortNumpy(xi, col):
    x_2 = cp.deepcopy(xi)
    temp = []
    for i in range(len(x_2)):
        temp.append(np.argsort(x_2[i]))
    if col == 0:
        for j in range(0, len(temp)):
            result[x1[j]: x1[j + 1], col] = temp[j]
    if col == 1:
        for j in range(0, len(temp)):
            result[x1[j]: x1[j + 1], col] = temp[j]
    return temp


def dendall(te, xone, col):
    tempand = cp.deepcopy(te)
    caps = cp.deepcopy(te)
    print("tempand"+ str(col), tempand)
    coplex = []
    dependency = []
    for i in range(len(t1)):
        for j in range(len(t1[i])):
            caps[i][j] = 0

    for i in range(len(tempand[:])):
        for j in range(1, len(tempand[i])):
            if col == 3:
                caps[2][5] = 1
            if tempand[i][j - 1] > tempand[i][j]:
                value = tempand[i][j - 1] - tempand[i][j]
                caps[i][j - 1] = value
                if col == 2:
                    coplex.append(i)
                    coplex.append(j)
                    coplex.append(value)
                if col == 3:
                    coplex.append(i)
                    coplex.append(j)
                    coplex.append(value)
                lenth = len(caps[i])
                back = caps[i][j - 1]
                dependency.append(((((lenth * (lenth - 1)) / 2) - back) - back) / ((lenth * (lenth - 1)) / 2))
    coplex = np.reshape(coplex, (-1, 3))
    for j in range(0, len(caps)):
        result[xone[j]: xone[j + 1], col] = caps[j]
    print("coplex" + str(col), coplex)
    print("dependency" + str(col), dependency)
    print("caps" + str(col), caps)
    return dependency, coplex


if __name__ == '__main__':

    numberMethod(x_data, df)
    t1 = sortNumpy(x2, 0)
    dep1, cop1 = dendall(t1, x1, 2)
    t2 = sortNumpy(x3, 1)
    dep2, cop2 = dendall(t2, x1, 3)
    print("x1", x1)
    print("x2", x2)
    print("x3", x3)
    # print("result:", result)·
    print(x_data[5:10, 1])
    name = []
    renp = np.reshape(result[:, 2], (1, -1))
    for i in x1:
        name.append(df["催化剂组合编号"][i])
    print(len(name))
    dfx = pd.DataFrame(np.ones((2, len(name))), columns=name)
    for i in range(len(cop1)):
        if i < 13:
            dfx.loc[0, str("A") + str(cop1[i][0] + 1)] = dep1[i]
    for i in range(len(cop2)):
        if i < 13:
            dfx.loc[1, str("A") + str(cop2[i][0] + 1)] = dep2[i]
            dfx.loc[1, "B4"] = dep2[5]
            dfx.loc[1, "A18"] = 1.0
    print("dfxtable", dfx)
    plotarry = np.asarray(dfx)
    print(name)
    print("dfx", plotarry)
    y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    print(y)
    plt.title("Group-A")
    plt.xlabel("Group(ax)")
    plt.ylabel("dependency")
    plt.plot(plotarry[0, 0:14], scaley=y, lw=3, label='CH3CH2OH')
    plt.plot(plotarry[1, 0:14], scaley=y, lw=3, label='C4=')
    plt.legend()
    plt.savefig("./img/Group-A.jpg")
    plt.show()


    plt.title("Group-B")
    plt.xlabel("Group(bx)")
    plt.ylabel("dependency")
    plt.plot(plotarry[0, 14:21], scaley=y, lw=3, label='CH3CH2OH')
    plt.plot(plotarry[1, 14:21], scaley=y, lw=3, label='C4=')
    plt.legend()
    plt.savefig("./img/Group-B.jpg")
    plt.show()

