# pandas-write2.py


#delete column
#http://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe

#preserve dataframe
#http://stackoverflow.com/questions/36743563/preserve-dataframe-column-data-type-after-outer-merge


#example
#http://xlsxwriter.readthedocs.io/example_pandas_simple.html

#https://www.getdatajoy.com/learn/Read_and_Write_Excel_Tables_from_Python




#panda courses
#https://github.com/jvns/pandas-cookbook
#https://github.com/guipsamora/pandas_exercises
#https://github.com/brandon-rhodes/pycon-pandas-tutorial

#http://xlsxwriter.readthedocs.io/working_with_dates_and_time.html


import pandas as pd


# Create a Pandas dataframe from some data.
# df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
df = pd.read_excel('staq2.xlsx', sheetname='Sheet1')
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter',date_format='mm/dd/yy')
# workbook = writer.book
# worksheet = writer.sheets['Sheet1']
# revenue_format = workbook.add_format({'num_format': '0.00'})
# worksheet.set_column('G:G',None,revenue_format)
# df.drop('',axis=1,inplace=True)
# df.drop(df.columns[0],axis=1)
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()