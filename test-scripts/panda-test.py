import pandas as pd
 
table = pd.read_excel('staq2.xlsx',
                      sheetname = 'Sheet1',
                      header = 0,
                      index_col = 0,
                      parse_cols = "A, B, C, D, E, F, G, H",
                      convert_float = True)
 
print(table)