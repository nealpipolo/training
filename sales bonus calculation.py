# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 08:55:43 2020

@author: npipolo
"""


import pandas as pd 
import numpy as np

# Columns needed for dataframe 
columns = ['Actual Sales', 'Salary' , 'Bonus Percent']

# Read in Excel file from directory using columns above
sales_df = pd.read_excel('C:/Users/npipolo/Desktop/sales_goal.xlsx', usecols=columns, sheet_name='Sheet1')

# Calculate Bonus as a New Column Called Bonus Amount
sales_df['Bonus Amount'] = sales_df['Salary'] * sales_df['Bonus Percent']

# Use Bonus Amount from Above to create a Total Pay Column
sales_df['Total Pay'] = sales_df['Salary'] + sales_df['Bonus Amount']

# If the Bonus is greater than or equal to 10,000  put big in a new column Dimension or small for less
sales_df['Bonus Size'] = np.where(sales_df['Bonus Amount'] >=10000, 'Big', 'Small')

# Create Source File Name 
sales_df['Source Name'] = ('Sales goal')

print(sales_df)

columns2 = ['Actual Sales' , 'Salary' , 'Bonus Percent']

sales_df_2 = pd.read_excel('C:/Users/npipolo/Desktop/sales_goal_two.xlsx', usecols=columns2, sheet_name='Sheet1')

sales_df_2['Bonus Amount'] = sales_df_2['Salary'] * sales_df_2['Bonus Percent']

sales_df_2['Total Pay'] = sales_df_2['Salary'] + sales_df_2['Bonus Amount']

sales_df_2['Bonus Size'] = np.where(sales_df['Bonus Amount']>=10000, 'Big', 'Small')

sales_df_2['Source Name'] = ('Sales goal two')

print(sales_df_2)

combined = pd.concat([sales_df, sales_df_2])

print (combined)

# write dataframe
combined.to_excel("C:/Users/npipolo/Desktop/combined.xlsxc.xlsx", header=True, index=True)

