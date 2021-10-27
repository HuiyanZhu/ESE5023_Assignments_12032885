# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:18:18 2021

@author: ZHY
"""

import numpy as np
import pandas as pd
#from matplotlib import pyplot as plt

#读取CSV文件并查看
Sig_Eqs = pd.read_csv('earthquakes-2021-10-22_21-12-33_+0800.tsv',sep='\t')
Sig_Eqs

#1.1
print(Sig_Eqs['Deaths'].sum())
Sig_Eqs.groupby('Country').sum('Total Deaths').sort_values('Total Deaths',ascending = False).head(10)

#1.2
m = Sig_Eqs.loc[(Sig_Eqs['Mag'] >  6.0)].groupby('Year').count()
m['Country'].plot(figsize=(15,10)) #python图片调整参考https://www.cnblogs.com/qbdj/p/11010773.html

#1.3
def CountEq_LargestEq(country_input):
    a = Sig_Eqs.loc[(Sig_Eqs['Country'] == country_input)].shape[0]
    b = Sig_Eqs.loc[(Sig_Eqs['Country'] == country_input)].sort_values('Mag').head(2)
    c = str(int(b.iat[0,1]))+'-'+str(b.iat[0,2])+'-'+str(b.iat[0,3])#Python读取指定位置的值参考https://blog.csdn.net/weixin_43474731/article/details/101530103中的df.iat()函数
    print('the total number of earthquakes since 2150 B.C. in '+country_input+' is '+str(a))
    print('the date of the largest earthquake ever happened in '+country_input+' is '+str(c))

Sig_Eqs = pd.read_csv('earthquakes-2021-10-22_21-12-33_+0800.tsv',sep='\t')
Sig_Eqs = Sig_Eqs.drop(index=0)
Sig_Eqs = Sig_Eqs.drop(index=6271)
country_input_array = Sig_Eqs['Country'].apply(str).unique() #因为Country有重复性，所以参考https://www.delftstack.com/zh/howto/python-pandas/pandas-unique-values-in-column/中的df.unique()函数，并参考https://www.delftstack.com/zh/howto/python-pandas/how-to-convert-pandas-dataframe-column-to-string/将Country转换为字符串，方便后续对国家进行倒序排序
country_input_array_sorted = sorted(country_input_array,key = str.lower,reverse=True)#Python中对字符串进行排序，且让其对大小写不敏感，参考https://blog.csdn.net/weixin_32000561/article/details/112938027
country_input_array_sorted = np.array(country_input_array_sorted)
for x in country_input_array_sorted:
    country_input = x
    CountEq_LargestEq(country_input)

