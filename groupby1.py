import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
                     'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
            'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
            'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data,index=['00','01','02','03','04','05','06','07','08','09','010','011'])

print (df)
a =df.groupby('Team')

print(df.groupby('Team').groups)
print(a.get_group("Kings"))


a1 = df.groupby('Year')
print(df.groupby('Year').groups)

print(a1.get_group(2014))


