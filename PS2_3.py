# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:56:22 2021

@author: ZHY
"""


import pandas as pd

#3.1
working_directory = pd.read_csv('2281305.csv')
working_directory
data = working_directory[['DATE','TMP']]
data
data1 = data['DATE'].str.split('-',expand=True)
data2 = data['TMP'].str.split(',',expand = True)
data3 = pd.merge(data1,data2,left_index=True,right_index=True)
data3.columns=['Year','Month','Daytime','Air_temperature','Air_temperature_quality_code']
data4 = data3.drop(columns='Daytime')
data4 = data4.astype('int')
data5 = data4[~data4['Air_temperature'].isin([+9999])]
data6 = data5.drop(index=data5[data5['Air_temperature_quality_code']!='1'].index[0])
data_final = data6.drop(columns='Air_temperature_quality_code')
data_final

#3.2
ave = data_final.groupby(['Year','Month']).agg('mean')
ave.plot.bar(figsize=(40,10))

#3.3
ave1 = data_final.groupby(['Month','Year']).agg('mean')
ave1.plot.bar(figsize=(10,10))