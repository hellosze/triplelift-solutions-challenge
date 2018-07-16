import pandas as pd
import numpy as np
import datetime

file = 'Centro-BX-April-2017-Sheet1-csv.csv'
df = pd.read_csv(file)
# print(df)
df_stations = df.groupby(["Station","Device","Sales"],as_index=False).sum()
print(df_stations)



df_stations.to_csv('revenue_summary.csv', sep=',')

# 26,137.00
# 25513.35


#binning
#groupby
#https://chrisalbon.com/python/pandas_binning_data.html
#bucketing
#summarising
#aggregating
#classifying
#https://chrisalbon.com/python/pandas_dataframe_descriptive_stats.html
#mapping


#https://chrisalbon.com/python/pandas_apply_operations_to_groups.html

