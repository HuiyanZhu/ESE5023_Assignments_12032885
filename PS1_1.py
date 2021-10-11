# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:04:54 2021

@author: ZHY
"""

import random
a = round(random.uniform(1,100)) # 随机数生成参考https://blog.csdn.net/qq_32618817/article/details/80583746
b = round(random.uniform(1,100))
c = round(random.uniform(1,100))

print("a="+str(a),"b="+str(b),"c="+str(c))
if a > b: #python if语句参考https://www.runoob.com/python3/python3-if-example.html
    if b > c:
        print(a,b,c)
    elif a > c:
        print(a,c,b)
    else: print(c,a,b)
elif a < b:
    if b < c:
        print(c,b,a)
    elif b > c:
        if a > c: 
            print(a,c,b)
        else: print (c,a,b)
    elif b < c:
        print(c,b,a)
