import pandas as pd
import numpy as np

df= pd.DataFrame(np.random.randn(5,6),index=['A','B','C','D','E'],columns=['col1','col2','col3','col4','col5','col6'])
print(df)

df= df.reindex(['A','b','C','d','E','F'])
print(df)
print(df.isnull())
print(df['col1'].isnull())
print(df['col1'].sum())
df1= pd.DataFrame(index=['a1','b1','c1'],columns=['c1','c2','c3'])
print(df1['c1'].sum())
print(df1)

print(df.fillna(method='bfill'))
print(df.dropna())
print(df.dropna(axis=1))

df3 = pd.DataFrame({'one':[np.nan,20,30,40,50,2000], 'two':[1000,60,30,40,50,2000]})
print(df3.replace({2000:20,1000:10,30:3,40:4,np.nan:10}))

