# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:33:03 2021

@author: ZHY
"""

import numpy as np

M1 = np.random.randint(0,50,(5,10))#生成随机矩阵参考https://blog.csdn.net/furide/article/details/103363451
M2 = np.random.randint(0,50,(10,5))
print(M1)
print(M2)
M = []
for i in range(M1.shape[0]):#矩阵中行数与列数的表达参考https://www.cnblogs.com/Yanjy-OnlyOne/p/11298253.html
    x = []
    for k in range(M2.shape[1]):
        y = 0
        for j in range(M1.shape[1]):
                y += M1[i][j]*M2[j][k]
        x.append(y) 
    M.append(x)
print(M)                

