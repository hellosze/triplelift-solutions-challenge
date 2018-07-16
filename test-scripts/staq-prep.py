# import openpyxl
# from openpyxl import Workbook
# wb = openpyxl.load_workbook('staq2.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')


# write_to = Workbook()
# write_sheet = write_to.active
# write_sheet['B100'].value = "Test Advertiser"
# write_to.save('test.xlsx')


# from openpyxl import load_workbook
# from openpyxl import Workbook
# read_from = load_workbook('staq2.xlsx')
# read_sheet = read_from.active
# write_to = Workbook()
# write_sheet = write_to.active
# write_sheet['A1'] = read_sheet['A1'].value
# write_sheet['A1'].style = read_sheet['A1'].style
# write_to.save('temp.xlsx')


import pandas as pd
xls_file = pd.ExcelFile('staq2.xlsx')
print xls_file.sheet_names
# print xls_file.names