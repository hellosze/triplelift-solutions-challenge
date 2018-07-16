import pandas as pd
import numpy as np

df = pd.read_csv('new_regional_bmw_copydoc.csv')
#print(df[df['CTA_fontSize'] == '8px'])
df1 = df.loc[ (df['Region'] == 'Baltimore') & (df['Creative_set'] == 'set1') & (df['Model'] == 'two_series')]
print(df1['Deal_copy'].values[0])

