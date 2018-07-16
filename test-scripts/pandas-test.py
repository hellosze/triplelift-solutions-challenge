# from datetime import datetime
import datetime
import pandas as pd
import time


# Create a Pandas dataframe from some data.
# df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
df = pd.read_excel('staq2a.xlsx', sheetname='Sheet1',index_col=None)
# df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].apply(lambda dt: datetime.datetime(dt.year, dt.month, dt.day))
# Create a Pandas Excel writer using XlsxWriter as the engine.
# Convert the dataframe to an XlsxWriter Excel object.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
df.set_index(['Date'])

# df['Date'] = df['Date'].apply(lambda dt: datetime.datetime(dt.year, dt.month, dt.day).date())
# df['Date'] = pd.to_datetime(df['Date'],format='%m/%d/%Y',yearfirst=False,dayfirst=False,exact=False,unit='s')
df['Date'] = df['Date'].apply(lambda x: x.strftime('%m/%d/%Y'))
# df.loc[5,'Revenue'] = "9999"

# df.loc[1,'Date'] = "2016-01-01"
# df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
# d = df['Date'].to_pydatetime()
# df['Date'] = pd.to_pydatetime(df['Date'], format='%m/%d/%Y')
# df['Date'] = time.mktime(d.timetuple())
# df['Date'] = df['Date'] + 1

# df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
# df['Date'] =  pd.to_datetime(df['Date'], format='%d%b%Y:%H:%M:%S.%f')

# df['Date'] = pd.to_datetime(df['Date'].astype(int), unit='s')


df.to_excel(writer, sheet_name='Sheet1', index=False)
# df['Date'] = pd.to_datetime(df['Date'],format='%m/%d/%Y',yearfirst=False,dayfirst=False,exact=False,unit='s')


workbook = writer.book
worksheet = writer.sheets['Sheet1']

revenue_format = workbook.add_format({'num_format': '0.00'})
worksheet.set_column('G:G',None,revenue_format)



date_format = workbook.add_format({'num_format': 'mm/dd/yyyy'})
worksheet.set_column('A:A',None,date_format)


# df['Revenue'][1] = "9999"

# df['Date'] = df['Date'].dt.date
# df['Date'] = "2012"



# date_time = datetime.strptime('2016-11-01 00:00:00', '%Y-%m-%d %H:%M:%S')



#useless
# df.drop('',axis=1,inplace=True)
# df.drop(df.columns[0],axis=1)


# Close the Pandas Excel writer and output the Excel file.
writer.save()