import pandas as pd;
from openpyxl import Workbook
from openpyxl import load_workbook
import numpy as npy
import re as re

wb = load_workbook('Kozhikode_to_Ernakulam.xlsx')
sheet1 = wb['Sheet1']
df1 = pd.DataFrame(sheet1.values)
df1.columns = df1.iloc[0]
df1 = df1[1:]

df1['route'] = 'Kozhikode to Ernakulam'
df1['ID'] = df1.index + 1
print(df1)