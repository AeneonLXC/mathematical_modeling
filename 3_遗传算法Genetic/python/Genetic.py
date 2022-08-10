import numpy as np
import matplotlib.pyplot as plt

# 遗传算法
def initpop(popsize, chromlength):
    """
    Parameters
    ----------
    popsize :  TYPE
        种群的数目.
    chromlength : TYPE
        表示染色体的长度（二值数的长度）， 长度的大小取决于变量的二进制编码的长度     

    Returns 
    -------
    pop : TYPE
        随机种群

    """
    pop=np.round(np.random.rand(popsize,chromlength))
    return pop
    
def decodebinary(pop):
    """
    二进制数转十进制数函数
    Parameters
    ----------
    pop : TYPE
          初始化种群.

    Returns
    -------
    pop2 种群的染色体二进制数转十进制数

    """
    px,py = pop.shape
    pop1 = np.zeros((px,py))
    for i in range(py):
        pop1[:,i] = (2**(py-i-1))*pop[:,i]
    pop2=np.sum(pop1, 1)#对pop1向量的每行求和 标识位0代表每列求和，标识位1代表每行求和
    
    return pop2

def decodechrom(pop,spoint,length):
    """
    将二进制编码转化为十进制数
    Parameters
    ----------
    pop : TYPE
        DESCRIPTION.
    spoint : TYPE
        染色体的起始位.
    length : TYPE
        DESCRIPTION.

    Returns
    -------
    pop2 : TYPE
        DESCRIPTION.

    """
    #对于多个变量而言，如有两个变量，采用20为表示，每个变量10位，则第一个变量从1开始，另一个变量从11开始。本例为一个变量
    #这句话的意思就是加入目标函数需要两个变量，则我可将染色体的数量拆为两个，然后遗传迭代
    #值得注意的是，我的染色体的长度也要跟着变量的数量改变，呈倍数关系
    pop1=pop[:,spoint:spoint+length]
    pop2=decodebinary(pop1)
    
    return pop2

def encode(bestpop):
    """
    解码x的值

    Parameters
    ----------
    bestpop : TYPE
        最好的个体.

    Returns
    -------
    x : TYPE
        最优X的取值.

    """
    
    temp = decodebinary(pop)
    x=temp*15/32767
    return x

def calobjvalue(pop):
    """
    实现目标函数的计算
    Parameters
    ----------
    pop : TYPE
        种群.

    Returns
    -------
    objvalue : TYPE
        返回目标函数值.

    """
    temp = decodechrom(pop, 0, 15)
    x=temp*15/32767
    objvalue = 9*np.sin(5*x)+7*np.cos(4*x)
    objvalue = np.reshape(objvalue,(-1,1))#以行的形式输出
    return objvalue

def calfitvalue(objvalue):
    """
    计算个体的适应值，在calobjvalue已经计算好，需要将小于0的个体删除，方便后续的概率计算

    Parameters
    ----------
    objvalue : TYPE
        目标函数值.

    Returns
    -------
    fitvalue : TYPE
        个体适应值.

    """
    global Cmin
    Cmin = 0
    fitvalue = np.zeros((objvalue.shape[0],objvalue.shape[1]))
    px, py = objvalue.shape
    for i in range(px):
        if objvalue[i,0] + Cmin > 0:
            temp = objvalue[i,0] + Cmin
        else:
            temp = 0
        
        fitvalue[i,0]=temp
    return fitvalue

def selection(pop, fitvalue):
    """
    选择函数 选择复制，决定哪些个体可以进入下一代
    采用轮盘赌选择

    Parameters
    ----------
    pop : TYPE
        种群的个体.
    fitvalue : TYPE
        个体适应值.

    Returns
    -------
    newpop : dict
        新的种群.

    """
    totalfit = np.sum(fitvalue)
    fitvalue_pro = fitvalue / (totalfit + 0.000001)
    fitvalue_pro_cumnsum = np.cumsum(fitvalue_pro)
    fitvalue_pro_cumnsum = np.reshape(fitvalue_pro_cumnsum,(-1,1))#以行的形式
    
    px, py = pop.shape 
    #轮盘随机概率 从小到大排序
    ms = np.sort(np.random.rand(px,1),0)
    
    fitin = 1 - 1   #pop种群 第几代个体 因为python的下标从0开始。所以是第一代的索引是0 故用1-1
    newin = 1 - 1  #pop种群 第几代个体
    newpop_dict = {}
    #我愿称为[适者生存，优胜劣汰] while循环
    while newin <= px-1:
        if ms[newin, 0] < fitvalue_pro_cumnsum[fitin, 0]:
            newpop_dict[newin] = pop[fitin,:]
            newin += 1
        else:
            fitin += 1
    
    newpop = np.zeros((newin,py))
    for i in range(newin):
        newpop[i,:] = newpop_dict[i]
    
    return newpop
    


def crossover(pop, pc):
    """
    交叉算法 实现基因重组
    Parameters
    ----------
    pop : TYPE
        种群.
    pc : TYPE
        交叉概率.

    Returns
    -------
    newpop : TYPE
        DESCRIPTION.

    """
    px, py = pop.shape 
    newpop = np.zeros((px, py))
    # seletion_litst = [i for i in range(px)]
    # sl = seletion_litst[0:px:2]
    for i in range(px-1):
        #是否能够进行基因重组
        if pc > np.random.rand(1)[0]:
            cpoint = int(np.round(np.random.rand(1)[0] * py) - 1)
            if cpoint == 0:
                cpoint = 1
                
            newpop[i, :][0:cpoint] = pop[i, 0:cpoint]
            newpop[i, :][cpoint+1:py] = pop[i+1, cpoint+1:py]
            
            newpop[i+1, :][0:cpoint] = pop[i+1, 0:cpoint]
            newpop[i+1, :][cpoint+1:py] = pop[i, cpoint+1:py]
            
        else:
            newpop[i,:] = pop[i,:]
            newpop[i+1,:] = pop[i+1,:]
    
    return newpop

def mutation(pop, pm):
    """
    变异算法 实现基因突变

    Parameters
    ----------
    pop : TYPE
        种群.
    pm : TYPE
        变异概率.

    Returns
    -------
    newpop : TYPE
        新的变异种群.

    """
    px, py = pop.shape 
    newpop = np.zeros((px, py))
    
    for i in range(px):
        if pm > np.random.rand(1)[0]:
            mpoint = int(np.round(np.random.rand(1)[0] * py) - 1)
            if mpoint == 0:
                mpoint = 1
            newpop[i,:] = pop[i,:]
            if newpop[i, mpoint] == 0:
                newpop[i, mpoint] = 1

        newpop[i,:] = pop[i,:]
    return newpop

def best(pop, fitvalue):
    """
    最优的个体及其适应值
    Parameters
    ----------
    pop : TYPE
        种群.
    fitvalue : TYPE
        适应值.

    Returns
    -------
    bestindividual : 最大适应值
        DESCRIPTION.
    bestfit : TYPE
        最大适应值的个体.

    """
    px, py = pop.shape 
    bestindividual = pop[0,:]
    bestfit = fitvalue[0]
    
    for i in range(1,px):
        if fitvalue[i] > bestfit:
            bestindividual = pop[i,:]
            bestfit = fitvalue[i]
    
    return bestindividual,bestfit



    
if __name__ == "__main__":
    popsize=30; #群体大小
    chromlength=15; #字符串长度（染色体的长度）
    pc=0.7; #交叉概率 
    pm=0.005 #变异概率
    
    #初始化种群
    pop=initpop(popsize, chromlength)
    poptest=pop
    #开始迭代 
    epoch = 200
    
    x_ = []
    y_ = []
    
    for i in range(epoch):
        objvalue = calobjvalue(pop)     #计算目标函数值
        fitvalue = calfitvalue(objvalue)    #计算群体中每个个体的适应度
        
        newpop = selection(pop, fitvalue)
        newpop1 = crossover(newpop, pc)
        newpop2 = mutation(newpop1, pm)
        
        objvalue = calobjvalue(newpop2)     #计算目标函数值
        fitvalue = calfitvalue(objvalue)    #计算群体中每个个体的适应度
        
        bestindividual,bestfit = best(newpop2, fitvalue) #求出群体中适应值最大的个体及其适应值
        x_.append(bestfit)
        pop = newpop2
        
        plt.plot(x_, lw=3, label='funcotio_max_value_x')
        plt.show()
        
    reshape_best_infrivedual = np.reshape(bestindividual,(1,-1))#以行的形式
    best_x_value = encode(reshape_best_infrivedual)
    plt.plot(x_, lw=3, label='funcotio_max_value_x')
    plt.legend()
    plt.show()
    
    print("最好的个体是 ",bestindividual)
    print("函数：f(x) = 9sin(5x)+7cos(4x)的极值为 ",bestfit[0]) #最后拟合之后随便取一个值即可
    print("x的取值应为： ",best_x_value[0]) #最后拟合之后随便取一个值即可
    
    # plt.plot(fv2, lw=3, label='fv2')
    # plt.legend()
    # plt.show()
    
        
    
    