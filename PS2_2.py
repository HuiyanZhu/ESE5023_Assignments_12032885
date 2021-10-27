# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:27:45 2021

@author: ZHY
"""


import pandas as pd

working_directory = pd.read_csv('2281305.csv')
working_directory
#根据user guide 确定WND为风速风向数据列，故只将其和时间列放入新dataframe中
data = working_directory[['DATE','WND']]
data

data1 = data['DATE'].str.split('-',expand=True)#时间在原表格中是用‘-’连接，参考https://blog.csdn.net/liuweiyuxiang/article/details/90936521中的在python中对字符串进行切分
data2 = data['WND'].str.split(',',expand = True)#切分方式同上
data3 = pd.merge(data1,data2,left_index=True,right_index=True)#将上面两个dataframe参考http://c.biancheng.net/pandas/merge.html进行合并
#data_final.rename(columns={'0_x':'Year','1_x':'Month','0_y':'Wind_direction_angle','1_y':'Wind_direction_quality_code','2_y':'Wind_type_code','3':'Wind_speed_rate','4':'Wind_speed_quality_code',inplace = True}
data3.columns=['Year','Month','Daytime','Wind_direction_angle','Wind_direction_quality_code','Wind_type_code','Wind_speed_rate','Wind_speed_quality_code']#更改列名参考https://www.cnblogs.com/shida-liu/p/13096214.html#:~:text=Pandas%E4%B8%AD%E4%BF%AE%E6%94%B9DataFrame%E5%88%97%E5%90%8D.%20%E6%9C%89%E6%97%B6%E5%80%99%E7%BB%8F%E8%BF%87%E6%9F%90%E4%BA%9B%E6%93%8D%E4%BD%9C%E5%90%8E%E7%94%9F%E6%88%90%E7%9A%84DataFrame%E7%9A%84%E5%88%97%E5%90%8D%E7%A7%B0%E6%98%AF%E9%BB%98%E8%AE%A4%E7%9A%84%EF%BC%8C%E4%B8%BA%E4%BA%86%E5%88%97%E5%90%8D%E6%A0%87%E8%AE%B0%E5%B7%B2%E4%B8%8E%E7%90%86%E8%A7%A3%EF%BC%8C%E6%9C%89%E6%97%B6%E5%80%99%E6%88%91%E4%BB%AC%E4%BC%9A%E6%9C%89%E4%BF%AE%E6%94%B9%E5%88%97%E5%90%8D%E7%A7%B0%E7%9A%84%E9%9C%80%E6%B1%82%E3%80%82.%20%E6%8F%90%E4%BE%9B%E4%BF%AE%E6%94%B9%E5%88%97%E5%90%8D%E7%9A%84%E6%96%B9%E6%B3%95%E5%A6%82%E4%B8%8B%EF%BC%9A.%20%E5%81%87%E5%A6%82%E6%9C%89%E5%88%9D%E5%A7%8B%E7%9A%84DataFrame%E5%A6%82%E4%B8%8B.%20%3E%3E%3E%20import%20pandas%20as,2%205%208%202%203%206%209.%201.
data4 = data3.drop(columns='Wind_direction_angle').drop(columns='Wind_direction_quality_code').drop(columns='Wind_type_code').drop(columns='Daytime')
data4 = data4.astype('int')
#j = data4.shape[0]
#for i in range(j):
#data5 = data4.drop(index=data4[data4['Wind_speed_rate']==9999].index[0])
data5 = data4[~data4['Wind_speed_rate'].isin([9999])]#参考https://blog.csdn.net/luocheng7430/article/details/80330566删除含有缺失值9999的行
data6 = data5[data5['Wind_speed_quality_code'].isin([1])]
#data6 = data5.drop(index=data5[data5['Wind_speed_quality_code']!='1'].index[0])
data_final = data6.drop(columns='Wind_speed_quality_code')
#data_final = data6.astype('int')
data_final
#data4.dtypes

ave = data_final.groupby(['Year','Month']).agg('mean')
#pd.DataFrame(ave)
ave

ave.plot.bar(figsize=(40,10))