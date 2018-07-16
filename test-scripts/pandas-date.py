# pandas-date.py
import pandas as pd
data = pd.DataFrame({'test_date':pd.date_range('1/1/2011', periods=12, freq='M') })
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

data.test_date = data.test_date - pd.datetime(1899, 12, 31)

pd.core.format.header_style = None    
data.to_excel(writer, sheet_name='test', index=False)

workbook  = writer.book
worksheet = writer.sheets['test']

formatdict = {'num_format':'mm/dd/yyyy'}
fmt = workbook.add_format(formatdict)

worksheet.set_column('A:A', None, fmt)

writer.save()