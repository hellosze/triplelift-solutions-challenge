# Import modules
import pandas as pd

#df = pd.read_csv('BMW_West_dataFeedUpdate.csv')
df = pd.read_csv('../dataSources/central/copydoc.csv').dropna()
unique = df.Region.unique()
unique.sort()
new_array = ', '.join('"{0}"'.format(el) for el in unique)
# print(unique)
# print("','".join(unique))
print("copydoc")
print(new_array)

#'Cincinnati','Minneapolis','Columbus','Chicago','Cleveland','Dayton','Detroit','Pittsburgh','Kansas City','Indianapolis'


df = pd.read_csv('../dataSources/central/BMW_CENTRAL_dataFeedUpdate-06.13.csv').dropna()
unique = df.location.unique()
unique.sort()
new_array = ', '.join('"{0}"'.format(el) for el in unique)
# print(unique)
# print("','".join(unique))
print("datafeed")
print(new_array)

