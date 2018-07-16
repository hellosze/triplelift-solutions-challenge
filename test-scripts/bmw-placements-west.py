# Import modules
import pandas as pd

#df = pd.read_csv('BMW_West_dataFeedUpdate.csv')
df = pd.read_csv('../dataSources/west/cxw-missing-placements.csv').dropna()
unique = df.unique.unique()
unique.sort()
new_array = ', '.join('"{0}"'.format(el) for el in unique)
# print(unique)
# print("','".join(unique))

print(new_array)

print(unique[0])
#'Cincinnati','Minneapolis','Columbus','Chicago','Cleveland','Dayton','Detroit','Pittsburgh','Kansas City','Indianapolis'


df = pd.read_csv('../dataSources/west/final/BMW-CXW-DCO-Feed-June-QA-v2.csv').dropna()
uniqueFeed = df.placement_id.unique()
uniqueFeed.sort()
new_array = ', '.join('"{0}"'.format(el) for el in uniqueFeed)
# print(unique)
# print("','".join(unique))
# print("datafeed")
# print(new_array)
# print(uniqueFeed)

print("QA")
_el = 147107611
convertedFeed = []
for el in uniqueFeed:
	# print(int(el))
	convertedFeed.append(int(el))
for el in unique:
	if int(el) in convertedFeed:
		print("Not missing:" +int(el))
# print(int(unique[0]) in convertedFeed)