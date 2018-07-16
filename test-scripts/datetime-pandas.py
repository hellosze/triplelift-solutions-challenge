import datetime
import pandas as pd
import time


# Create a Pandas dataframe from some data.
# df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
df = pd.read_excel('staq2a.xlsx', sheetname='Sheet1',index_col=None)
# df[(df['Date'].dt.month == 11) & (df['Date'].dt.day == 1)]

df['Date'] = df['Date'].apply(lambda dt: datetime.datetime(dt.year, dt.month, dt.day))
