# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 14:31:33 2021

@author: ZHY
"""
#import numpy as np

# #def Pascal_triangle(k):
# #    j = int(k)
# #    m = []
# #   if j == 1:
#     #     m.append(1)
#     #     print(m)
#     # elif j == 2:
#     #     m.append(1)
#     #     m.append(1)
#     #     print(m)
#     # elif j > 2:
#     #     m = [1,1]
#     #     y = [1,1]
#     #     for n in range(j-2):
#     #         for i in range(n+1):
#     #             x = int(m[i]+m[i+1])
#     #         m.insert(i+1,x)
#     #     y.insert(n+1,x)
        
               
                
#     #     print(y)
#     else:
# #        print("invalid k value")
# #        
# #        
# #Pascal_triangle(4)

# 以下代码受题目材料中 “a formula for any entry in the triangle" 启发:        
def Pascal_triangle(k):
    a = 1
    n=[]
    for b in range(1,k+1): #阶乘写法参考https://www.php.cn/python-tutorials-460228.html
        a *= b
    for i in range(k+1):
        c = 1
        e = 1
        for d in range(1,i+1):
            c *= d
        for f in range(1,k-i+1):
            e *= f
        m = int(a/(c*e)) # 此处不加int会导致输出结果带有一位小数
        n.append(m)
    print(n)
    
print("Pascal_triangle(100)"+Pascal_triangle(100))
print("Pascal_triangle(200)"+Pascal_triangle(200))    


j = int(input("If you want to know more, please enter the row number:"))
k = j-1
Pascal_triangle(k)





        
            
            
           
           
        
        
        