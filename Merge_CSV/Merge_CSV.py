#!/usr/bin/env python
# coding: utf-8

# In[8]:

import sys
import os
import pandas as pd
import glob
# df1Path = input("Enter Absolute File Path Of The First .xlsx:")
# df2Path = input("Enter Absolute File Path Of The Secound .xlsx:")
# matchingColumn = input("Enter The Column Name You Want To Use As A Primary key To Merge All Data:")
# outputPath = input("Enter Your .csv Absolute Output Path:")


# df1Path = sys.argv[1]
# df2Path = sys.argv[2]

if len(sys.argv) == 1:
    matchingColumn = 'Citizen ID'
else:
    matchingColumn = sys.argv[1]

outputPath = '..\\Merge_CSV\\out\\MergeOutput.csv'

print('matchingColumn = ' + matchingColumn)
df1dir = r'..\Merge_CSV\input1' # use your path
df1file = glob.glob(df1dir + "/*")
df1Path = ''

for filename in df1file:
    df1Path = filename

df2dir = r'..\Merge_CSV\input2' # use your path
df2file = glob.glob(df2dir + "/*")
df2Path = ''

for filename in df2file:
    df2Path = filename
    
print(df1Path)
print(df2Path)
# In[10]:

type_csv = ".csv"
type_xlsx = ".xlsx"
type_xls = ".xls"

print("Start Loading input")
if type_xlsx in df1Path or type_xls in df1Path:
    try:
        print("Load first Dataframe.....")
        df = pd.read_excel(f'{df1Path}') 
        print("Success")
    except FileNotFoundError:
        print('Error code 1: File 1 does not exist, press enter to continue')
        input()
elif type_csv in df1Path:
    try:
        print("Load First Dataframe.....")
        df = pd.read_csv(f'{df1Path}')
        print("Success")
    except FileNotFoundError:
        print('Error code 1: File 1 does not exist, press enter to continue')
        input()
else:
    raise ValueError("Error code 2: File type invalid, press enter to continue")
    input()
# In[11]:
if type_xlsx in df2Path or type_xls in df2Path:
    try:
        print("Load secound Dataframe.....")
        df2 = pd.read_excel(f'{df2Path}')
        print("Success")
    except FileNotFoundError:
        print('Error code 1: File 2 does not exist, press enter to continue')
        input()
elif type_csv in df2Path:
    try:
        print("Load secound Dataframe.....")
        df2 = pd.read_csv(f'{df2Path}')
        print("Success")
    except FileNotFoundError:
        print('Error code 1: File 2 does not exist, press enter to continue')
        input()
else:
    raise ValueError("Error code 2: File type invalid, press enter to continue")
    input()

print("All Dataframe was successfully loaded ●ヽ(ﾟ∀ﾟ)ﾉ●")


# In[12]:

print("Validate matching column")
if not matchingColumn in df.columns:
    raise ValueError("Error code 3: No sunch Column in df, press enter to continue")
    input()

if not matchingColumn in df2.columns:
    raise ValueError("Error code 3: No sunch Column in df2, press enter to continue")
    input()

print("Validate complete, column is valid")


# In[5]:


print('Start merging data')
df3 = pd.merge(df, df2, on = matchingColumn ,how='inner',copy=False)
print('Merge complete')
print('Start cleansing data')
df3.drop(df3.filter(regex="Unname"),axis=1,inplace=True)
df3.drop(df3.filter(regex="_y"),axis=1,inplace=True)
df3.columns = df3.columns.str.rstrip('_x')
df3 = df3.dropna(how='any',axis=0) 
print('Cleansing data complete')

# In[6]:

print('Start writing an output file.....')
df3.to_csv(f'{outputPath}',index = False,encoding='utf-8-sig')
print('Output file was successfully written, press enter to continue (＾• ω •＾)')

# In[ ]:




