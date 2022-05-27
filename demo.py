import numpy as np
import pandas as pd

#series
s = pd.Series([1,2,3.0,"asdf"])
print(s)

#date_range
d = pd.date_range('20220401',periods=7)
print(d)

#dataframe with random values
df = pd.DataFrame(np.random.randn(7,4), index=d, columns=['A','B','C','D'])
print(df)

#dataframe with dictonary of objects
df1 = pd.DataFrame({'A':[1,2,3,4],
                    'B':pd.Timestamp('20220401'),
                    'C':pd.Series(2,index=list(range(4)),dtype='int'),
                    'D':np.array([5]*4,dtype='int32'),
                    'E':pd.Categorical([0,1,0,1]),
                    'F':'edureka'

})

print(df1)


df2 = pd.read_csv("/Users/chetanrao/PycharmProjects/archive/country_vaccinations_by_manufacturer.csv")

print(df1.dtypes)
df1.head(2)
