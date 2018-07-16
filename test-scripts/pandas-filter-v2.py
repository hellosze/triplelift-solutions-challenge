import pandas as pd


data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'year': [2012, 2012, 2013, 2014, 2014],
        'reports': [4, 24, 31, 2, 3],
        'coverage': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
# df = pd.DataFrame(data)
#print(df)

df1 = df['coverage'] > 50
# df[df1]['Pima'] = 123
df.loc[df1,'coverage'] = 123
year_df = df['year'] == 2014
df.loc[year_df,'year'] = 1999
# print(df1)
print(df1)
#df[df['coverage'] > 50] = 123
#print(df['coverage'])

df2 = df[df1]
df2.to_csv('out.csv', sep=',')
