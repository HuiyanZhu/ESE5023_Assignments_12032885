# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:14:16 2021

@author: ZHY
"""

import random
x = int(random.randint(1,100))
print("The random value is:"+str(x))

i = 0
if x != 1 or 2 or 3:
    while x >= 2:
        if x % 2 == 0:
            i += 1
            x = x/2
        else:
            i += 1
            x = x-1
        
        
    #     if x >= 2:
    #         i += 1
    #         x = x/2
    #         continue
    # elif x % 2 != 0:
    #     if x >= 1:
    #         i += 1
    #         x = x-1
    #         continue


    # while x % 2 != 0:
    #     if x >= 1:
    #         i += 1
    #         x = x-1
        # while x % 2 == 0:
        #     if x >= 2:
        #         i += 1
        #         x = x/2
        # else:
        #     x = x-1
        #     i += 1
        #     while x % 2 == 0:
        #         if x >= 2:
        #             i += 1
        #             x = x/2
        #     else:
        #         x = x-1
        #         i += 1
        #         while x % 2 == 0:
        #             if x >= 2:
        #                 i += 1
        #                 x = x/2
        #         else:
        #             x = x-1
        #             i += 1
    print(i)
elif x == 1:
    print("0")
elif x == 2:
    print("1")
else:
    print("2")
    
        