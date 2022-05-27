import pandas as pd
import numpy as np

d={'col1':[11,2,30,15],
   'col2':[12,3,4,11],
   'col3':[32,4,50,13],
   'col4':[51,5,60,18]}
df = pd.DataFrame(data=d, dtype=np.int16)
print(df)
print(df.dtypes)

d2 ={'col1':[1,2,3],
     'col2':pd.Series([2,3],index=[1,2]),
     'col3':[4,5,6]}
df1 = pd.DataFrame(data=d2,index=[0,1,2])
print(df1)
print(df1.dtypes)

print(df1.index)

print(df.to_numpy())
print(df.describe())

print(df.sort_values(by='col3'))
print(df['col2'])

print(df[1:4])
print(df.loc[2:3,['col1','col2']])

print(df.iloc[3])

print(df.iloc[1:3,0:2])

print(df[df['col1']>10])

d = pd.date_range('20200401',periods=10)
print(d)
df20 = pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])
print(df20)





