# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 08:55:43 2020

@author: npipolo
"""


import pandas as pd 
import numpy as np


columns = ['Actual Sales', 'Salary' , 'Bonus Percent']

sales_df = pd.read_excel
('C:/Users/npipolo/Desktop/sales_goal.xlsx'
 , usecols=columns
 , sheet_name='Sheet1')

sales_df['Bonus Amount'] 
= sales_df['Salary'] * 
sales_df['Bonus Percent']

sales_df['Total Pay'] = 
sales_df['Salary'] 
+ sales_df['Bonus Amount']


sales_df['Bonus Size'] = 
np.where(sales_df['Bonus Amount']
         >=10000, 'Big', 'Small')

print(sales_df)


columns2 = ['Actual Sales' , 'Salary' , 'Bonus Percent']

sales_df_2 = pd.read_excel('C:/Users/npipolo/Desktop/sales_goal_two.xlsx', usecols=columns2, sheet_name='Sheet1')

print(sales_df_2)


