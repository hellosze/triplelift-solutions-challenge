import pandas as pd
import numpy as np

df = pd.read_csv('BMW_EAST_dataFeedUpdate.csv')
#print(df[df['CTA_fontSize'] == '8px'])


df300x600 = (df['dimension'] == '300x600')
df300x250 = (df['dimension'] == '300x250')
df970x250 = (df['dimension'] == '970x250')

df728x90 = (df['dimension'] == '728x90')
df160x600 = (df['dimension'] == '160x600')

dfBaltimore = (df['location'] == 'Baltimore')
dfHartford = (df['location'] == 'Hartford')
dfProvidence = (df['location'] == 'Providence')
dfHarrisburg = (df['location'] == 'Harrisburg')
dfBoston = (df['location'] == 'Boston')
dfWilkesBarre = (df['location'] == 'Wilkes Barre')
dfWestSpringfield = (df['location'] == 'West Springfield')
dfDC = (df['location'] == 'Washington DC')
dfNewHampshire = (df['location'] == 'New Hampshire')
dfNorfolk = (df['location'] == 'Norfolk')
dfTriState = (df['location'] == 'Tri-State')
dfPhiladelphia = (df['location'] == 'Philadelphia')
# baltimore = df[ (df['location'] == 'Baltimore') & (df['dimension'] != '320x50') & (df['dimension'] != '300x50')]

df2Series = (df['Model'] == 'two_series')
df3Series = (df['Model'] == 'three_series')
df4Series = (df['Model'] == 'four_series')
df4SeriesCoup = (df['Model'] == 'four_series_coup')
df5Series = (df['Model'] == 'five_series')
df6Series = (df['Model'] == 'six_series')
df7Series = (df['Model'] == 'seven_series')
dfi3Series = (df['Model'] == 'i3')
dfX1Series = (df['Model'] == 'X1')
dfX3Series = (df['Model'] == 'X3')
dfX4Series = (df['Model'] == 'X4')
dfX5Series = (df['Model'] == 'X5')
dfX6Series = (df['Model'] == 'X6')




# print(baltimore)
#print(df.dtypes.index)


# df1 = df['coverage'] > 50
# df[df1]['Pima'] = 123
df.loc[(dfBaltimore & df300x250) | (dfBaltimore & df300x600) | (dfBaltimore & df970x250),'CTA_text'] = 'UMJ3'



df.to_csv('BMW_EAST_dataFeedUpdate-06-06-2017.csv', sep=',')