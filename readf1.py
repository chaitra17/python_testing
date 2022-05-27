import numpy as np
import pandas as pd

df = pd.read_csv("/Users/chetanrao/PycharmProjects/archive/country_vaccinations.csv")


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

newdf = df.select_dtypes(include=numerics)
print(newdf)
print(df)
print(df.columns)
print(df.describe())

numeric1 = ['int16','int32', 'int64','float16', 'float32', 'float64']

n2 = df.select_dtypes(include=numeric1)
print(n2)
print(len(n2.columns))
print(n2.info())

#how do we find missing values in pandas
print(df.isna().sum().sort_values(ascending=False))
missing_per = (df.isna().sum().sort_values(ascending=False)/len(df))*100
print(missing_per)
print(type(missing_per))
