# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:05:51 2022

@TwinkelStar: 一直闪闪发光的李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#               动态规划算法案例 
#               Coding By lxc
#                  
#
#          LAST_UPDATE: Fri Aug 12 10:05:51 2022
#
# ----------------------------------------------

"""
import numpy as np

#创建工人列表
person = np.array(
    [[15,18,21,24],
     [19,23,22,18],
     [26,17,16,19],
     [19,21,23,17]
     ])

#创建决策表
decision = np.zeros((person.shape[0],person.shape[1]))

lower = min(person[:,0]) + min(person[:,1]) + min(person[:,2]) + min(person[:,3])

for i in range(1,decision.shape[0]):
    for j in range(1,lower):
        

        

