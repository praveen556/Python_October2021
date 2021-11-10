
# Importing Library for Reading Excel
import xlrd
import pandas as pd

df = pd.read_excel(r"C:\Users\prave\github\Python_October2021\data\Contract_Examples.xlsx")

print(df.row(0))
