# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 09:21:44 2021

@author: ZHY
"""
# #test1
# # import random
# # num = [1,2,3,4,5,6,7,8,9]
# num = "1 2 3 4"
# i = 0
# while i < 3:
#       h = 0
#       while h < 3:
#         if i == 0:
#             num = num[:5-2*h] + "+" + num[6-2*h:]
#             # print(n)
#         elif i == 1:
#             num = num[:5-2*h] + "-" + num[6-2*h:]
#             # print(n)
#         elif i == 2:
#             num = num[:5-2*h] + " " + num[6-2*h:]
#             # print(n)
#         h += 1
#         print(num)
#     # print(num)
#       i += 1
#     # print(num)
# # print(num)

# #test2
# num = "1 2 3 4"
# i=0
# while i < 3:
#     j = 0
#     while j < 3:
#         if i == 0:
#             num = num[:5-2*i] + "+" + num[6-2*i:]
#             # print(n)
#         elif i == 1:
#             num = num[:5-2*i] + "-" + num[6-2*i:]
#             # print(n)
#         elif i == 2:
#             num = num[:5-2*i] + " " + num[6-2*i:]
#         i += 1
#         k = 0
#         while k < 3:
#             if j == 0:
#                 num = num[:5-2*j] + "+" + num[6-2*j:]
#             # print(n)
#             elif j == 1:
#                 num = num[:5-2*j] + "-" + num[6-2*j:]
#             # print(n)
#             elif j == 2:
#                 num = num[:5-2*j] + " " + num[6-2*j:]
#             j += 1
#             k+=1
#             # print(n)
#     # i += 1
#     print(num)

# # test3
# num = "1 2 3 4"
# n = ["+","-"," "]
# p = ["-"," ","+"]
# q = [" ","+","-"]
# # i = 0
# # while i < 3:
# j = 0
# while j < 3:
#         # l = 0
#         # for l in range(3):
#     if j == 0:
#         for k in range(3):
#             for l in range(5,0,-2):
#                 num = num[:l] + n[k] + num[l+1:]
#                 print(num)
#         # num = "1 2 3 4"
                
#     elif j == 1:
#         for k in range(3):
#             for l in range(5,0,-2):
#                 num = num[:l] + p[k] + num[l+1:]
#                 print(num)
#         # num = "1 2 3 4"
#     elif j == 2:
#         for k in range(3):
#             for l in range(5,0,-2):
#                 num = num[:l] + q[k] + num[l+1:]
#                 print(num)
#         # num = "1 2 3 4"
#     j += 1
#     # i += 1
#     # i += 1
#     # print(num)

# # test4
# num = "1 2 3 4"
# n = ["+","-"," "]
# for i in range(3):
#     num = num[:5] + n[i] + num[6:]
#     # print(num)
#     for j in range(3):
#         num = num[:3] + n[j] + num[4:]
#         # print(num)
#         for k in range(3):
#             num = num[:1] + n[k] + num[2:]
#             print(num)


# FINAL-5.1
import random
# i = random.randint(1, 101)
def Find_expression(i):
    num = "1 2 3 4 5 6 7 8 9"
    n = ["+","-"," "]
    k = 0
# j = 0
    for a in range(3):
        num = num[:15] + n[a] + num[16:]
        for b in range(3):
            num = num[:13] + n[b] + num[14:]
            for c in range(3):
                num = num[:11] + n[c] + num[12:]
                for d in range(3):
                    num = num[:9] + n[d] + num[10:]
                    for e in range(3):
                        num = num[:7] + n[e] + num[8:]
                        for f in range(3):
                            num = num[:5] + n[f] + num[6:]
                            for g in range(3):
                                num = num[:3] + n[g] + num[4:]
                                for h in range(3):
                                    num = num[:1] + n[h] + num[2:]
                                # print(num)
#                                 j += 1     #测试总个数是否为3^8
# print(j)
                                    m = num.replace(" ","")
                                # print(m)
                                    x = eval(m)#计算字符串形式的数学运算参考https://blog.csdn.net/llb19900510/article/details/109527054
                                # print(x)
                                    if x == i:
                                        print(str(m) + "=" +str(x))
                                        k += 1
    #print(k)                                        
i = random.randint(1, 101)
Find_expression(i)                                
                                
#5.2
import matplotlib.pyplot as plt
Y = []
X = []
def Total_solutions(i):
    num = "1 2 3 4 5 6 7 8 9"
    n = ["+","-"," "]
    k = 0
    # y = []
# j = 0
    for a in range(3):
        num = num[:15] + n[a] + num[16:]
        for b in range(3):
            num = num[:13] + n[b] + num[14:]
            for c in range(3):
                num = num[:11] + n[c] + num[12:]
                for d in range(3):
                    num = num[:9] + n[d] + num[10:]
                    for e in range(3):
                        num = num[:7] + n[e] + num[8:]
                        for f in range(3):
                            num = num[:5] + n[f] + num[6:]
                            for g in range(3):
                                num = num[:3] + n[g] + num[4:]
                                for h in range(3):
                                    num = num[:1] + n[h] + num[2:]
                                # print(num)
#                                 j += 1     #测试总个数是否为3^8
# print(j)
                                    m = num.replace(" ","")
                                # print(m)
                                    x = eval(m)#计算字符串形式的数学运算参考https://blog.csdn.net/llb19900510/article/details/109527054
                                # print(x)
                                    if x == i:
                                        # print(str(m) + "=" +str(x))
                                        k += 1
                                   
    Y.append(k)
    X.append(i)

for i in range(1,101):
    Total_solutions(i)
print(X)
print(Y)

plt.plot(X,Y,marker='o',linestyle='dashed')
plt.show()
print("based on the plot,1 and 47 yield the maximum Total_solutions(26) and 90 yields the minimum of Total_solutions(6)")



    
    
    















                                    
    # for b in range(3):
    #     for c in range(3):
    #         for d in range(3):
    #             for e in range(3):
    #                 for f in range(3):
    #                     for g in range(3):
                                                            