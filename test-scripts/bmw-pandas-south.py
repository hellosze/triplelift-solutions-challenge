import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('../dataSources/south/BMW_SOUTH_dataFeedUpdate-06.13.csv')
df.set_index('unique_id', inplace=True)
#print(df[df['CTA_fontSize'] == '8px'])
dfcopydoc = pd.read_csv('../dataSources/south/copydoc.csv')
dfUrls = pd.read_csv('../dataSources/south/urls.csv')
# print(dfUrls)


df300x600 = (df['dimension'] == '300x600')
df300x250 = (df['dimension'] == '300x250')
df970x250 = (df['dimension'] == '970x250')

df728x90 = (df['dimension'] == '728x90')
df160x600 = (df['dimension'] == '160x600')
df300x50 = (df['dimension'] == '300x50')
df320x50 = (df['dimension'] == '320x50')


regions = ["Atlanta", "Charlotte", "Greensboro", "Savannah", "Jacksonville", "Orlando", "Raleigh", "Miami", "WPB", "Dallas", "Ft Myers", "Greenville", "Gulf Coast", "Houston", "Tampa Bay", "Austin", "Baton Rouge", "Birmingham", "Charleston", "Gainesville", "Melbourne", "Memphis", "Nashville", "New Orleans", "OKC", "San Antonio"
]
models = ["two_series", "three_series","four_series","four_series_coup","five_series","six_series","seven_series","i3","X1","X3","X4","X5","X6"]


# print(baltimore)
#print(df.dtypes.index)

dfWeight = (df['weighting'] == 0)
for region_index, bmw_region in enumerate(regions):
	for model_index, bmw_model in enumerate(models):
		dfLocalRegion = (df['location'] == bmw_region)
		dfLocalModel = (df['Model'] == bmw_model)
		dfUrl = dfUrls.loc[ (dfUrls['Region'] == bmw_region) & (dfUrls['Model'] == bmw_model)]
		# print("/" + regions_lut[region_index] + "/" + models_lut[model_index])
		# print(dfUrl['Exit_url'].values[0] + "/" + regions_lut[region_index] + "/" + models_lut[model_index])

		# print(dfcopydoc.loc[ (dfcopydoc['Region'] == regions_lut[region_index]) & (dfcopydoc['Creative_set'] == 'set1') & (dfcopydoc['Model'] == models_lut[model_index])])
		#set 1 - 300x250, 300x600, 970x250
		set1copy = dfcopydoc.loc[ (dfcopydoc['Region'] == bmw_region) & (dfcopydoc['Creative_set'] == 'set1') & (dfcopydoc['Model'] == bmw_model)]
		# print(dfUrl['Exit_url'].values[0])
		df.loc[(dfLocalModel & dfLocalRegion & df300x250) | (dfLocalModel & dfLocalRegion & df300x600) | (dfLocalModel & dfLocalRegion & df970x250),'CTA_text'] = set1copy['Deal_copy'].values[0]
		#set1copy['Deal_copy'].values[0]
		df.loc[(dfLocalModel & dfLocalRegion & df300x250) | (dfLocalModel & dfLocalRegion & df300x600) | (dfLocalModel & dfLocalRegion & df970x250),'is_active'] = set1copy['isActive'].values[0]
		df.loc[(dfLocalModel & dfLocalRegion & df300x250) | (dfLocalModel & dfLocalRegion & df300x600) | (dfLocalModel & dfLocalRegion & df970x250),'weighting'] = int(set1copy['Weight'].values[0]) or 1
		df.loc[(dfLocalModel & dfLocalRegion & df300x250) | (dfLocalModel & dfLocalRegion & df300x600) | (dfLocalModel & dfLocalRegion & df970x250),'exit_URL'] = dfUrl['Exit_url'].values[0]
		df.loc[(dfLocalModel & dfLocalRegion & df300x50) | (dfLocalModel & dfLocalRegion & df320x50),'exit_URL'] = dfUrl['Exit_url'].values[0]
		
		#set 2 - 728x90
		set2copy = dfcopydoc.loc[ (dfcopydoc['Region'] == bmw_region) & (dfcopydoc['Creative_set'] == 'set2') & (dfcopydoc['Model'] == bmw_model)]
		df.loc[(dfLocalModel & dfLocalRegion & df728x90),'CTA_text'] = set2copy['Deal_copy'].values[0]
		df.loc[(dfLocalModel & dfLocalRegion & df728x90),'is_active'] = set2copy['isActive'].values[0]
		df.loc[(dfLocalModel & dfLocalRegion & df728x90),'weighting'] = int(set2copy['Weight'].values[0]) or 1
		df.loc[(dfLocalModel & dfLocalRegion & df728x90),'exit_URL'] = dfUrl['Exit_url'].values[0]
		

		#set 3 - 160x600
		set3copy = dfcopydoc.loc[ (dfcopydoc['Region'] == bmw_region) & (dfcopydoc['Creative_set'] == 'set3') & (dfcopydoc['Model'] == bmw_model)]
		df.loc[(dfLocalModel & dfLocalRegion & df160x600) ,'CTA_text'] = set3copy['Deal_copy'].values[0]
		df.loc[(dfLocalModel & dfLocalRegion & df160x600) ,'is_active'] = set3copy['isActive'].values[0]
		df.loc[(dfLocalModel & dfLocalRegion & df160x600) ,'weighting'] = int(set3copy['Weight'].values[0]) or 1
		df.loc[(dfLocalModel & dfLocalRegion & df160x600) ,'exit_URL'] = dfUrl['Exit_url'].values[0]
		
		df.loc[dfWeight,'weighting'] = 1

today_timestamp = str(datetime.datetime.today()).split()[0] + "-" + str(datetime.datetime.today()).split()[1]
df.to_csv('../dataSources/south/BMW_SOUTH_dataFeedUpdate'+today_timestamp+'.csv', sep=',')

