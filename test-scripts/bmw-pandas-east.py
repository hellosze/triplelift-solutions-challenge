import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('../dataSources/east/BMW_EAST_dataFeedUpdate-06.13.csv')
df.set_index('unique_id', inplace=True)
#print(df[df['CTA_fontSize'] == '8px'])
dfcopydoc = pd.read_csv('../dataSources/east/new_regional_bmw_east_copydoc-v2.csv')
dfUrls = pd.read_csv('../dataSources/east/new_regional_bmw_east_urls.csv')



df300x600 = (df['dimension'] == '300x600')
df300x250 = (df['dimension'] == '300x250')
df970x250 = (df['dimension'] == '970x250')

df728x90 = (df['dimension'] == '728x90')
df160x600 = (df['dimension'] == '160x600')

df300x50 = (df['dimension'] == '300x50')
df320x50 = (df['dimension'] == '320x50')


dfBaltimore = (df['location'] == 'Baltimore')
dfHartford = (df['location'] == 'Hartford')
dfProvidence = (df['location'] == 'Providence')
dfHarrisburg = (df['location'] == 'Harrisburg')
dfBoston = (df['location'] == 'Boston')
dfWilkesBarre = (df['location'] == 'Wilkes Barre')
dfWestSpringfield = (df['location'] == 'West Springfield')
dfDC = (df['location'] == 'Washington DC')
dfNewHampshire = (df['location'] == 'New Hampshire')
dfNorfolk = (df['location'] == 'Norfolk')
dfTriState = (df['location'] == 'Tri-State')
dfPhiladelphia = (df['location'] == 'Philadelphia')
# baltimore = df[ (df['location'] == 'Baltimore') & (df['dimension'] != '320x50') & (df['dimension'] != '300x50')]

regions = [dfBaltimore,dfHartford,dfProvidence,dfHarrisburg,dfBoston,dfWilkesBarre,dfWestSpringfield,dfDC,dfNewHampshire,dfNorfolk,dfTriState,dfPhiladelphia]
regions_lut = ["Baltimore","Hartford","Providence","Harrisburg","Boston","Wilkes Barre","West Springfield", "Washington DC", "New Hampshire", "Norfolk", "Tri-State", "Philadelphia"]

df2Series = (df['Model'] == 'two_series')
df3Series = (df['Model'] == 'three_series')
df4Series = (df['Model'] == 'four_series')
df4SeriesCoup = (df['Model'] == 'four_series_coup')
df5Series = (df['Model'] == 'five_series')
df6Series = (df['Model'] == 'six_series')
df7Series = (df['Model'] == 'seven_series')
dfi3Series = (df['Model'] == 'i3')
dfX1Series = (df['Model'] == 'X1')
dfX3Series = (df['Model'] == 'X3')
dfX4Series = (df['Model'] == 'X4')
dfX5Series = (df['Model'] == 'X5')
dfX6Series = (df['Model'] == 'X6')

models = [df2Series,df3Series,df4Series,df4SeriesCoup,df5Series,df6Series,df7Series,dfi3Series,dfX1Series,dfX3Series,dfX4Series,dfX5Series,dfX6Series]
models_lut = ["two_series", "three_series","four_series","four_series_coup","five_series","six_series","seven_series","i3","X1","X3","X4","X5","X6"]


# print(baltimore)
#print(df.dtypes.index)

dfWeight = (df['weighting'] == 0)
for region_index, bmw_region in enumerate(regions):
	for model_index, bmw_model in enumerate(models):
		dfUrl = dfUrls.loc[ (dfUrls['Region'] == regions_lut[region_index]) & (dfUrls['Model'] == models_lut[model_index])]
		# print("/" + regions_lut[region_index] + "/" + models_lut[model_index])
		# print(dfUrl['Exit_url'].values[0] + "/" + regions_lut[region_index] + "/" + models_lut[model_index])
		# print(dfcopydoc.loc[ (dfcopydoc['Region'] == regions_lut[region_index]) & (dfcopydoc['Creative_set'] == 'set1') & (dfcopydoc['Model'] == models_lut[model_index])])
		#set 1 - 300x250, 300x600, 970x250
		set1copy = dfcopydoc.loc[ (dfcopydoc['Region'] == regions_lut[region_index]) & (dfcopydoc['Creative_set'] == 'set1') & (dfcopydoc['Model'] == models_lut[model_index])]

		df.loc[(bmw_model & bmw_region & df300x250) | (bmw_model & bmw_region & df300x600) | (bmw_model & bmw_region & df970x250),'CTA_text'] = set1copy['Deal_copy'].values[0]
		df.loc[(bmw_model & bmw_region & df300x250) | (bmw_model & bmw_region & df300x600) | (bmw_model & bmw_region & df970x250),'is_active'] = set1copy['isActive'].values[0]
		df.loc[(bmw_model & bmw_region & df300x250) | (bmw_model & bmw_region & df300x600) | (bmw_model & bmw_region & df970x250),'weighting'] = int(set1copy['Weight'].values[0]) or 1
		df.loc[(bmw_model & bmw_region & df300x250) | (bmw_model & bmw_region & df300x600) | (bmw_model & bmw_region & df970x250),'exit_URL'] = dfUrl['Exit_url'].values[0]
		df.loc[(bmw_model & bmw_region & df300x50) | (bmw_model & bmw_region & df320x50),'exit_URL'] = dfUrl['Exit_url'].values[0]

		#set 2 - 728x90
		set2copy = dfcopydoc.loc[ (dfcopydoc['Region'] == regions_lut[region_index]) & (dfcopydoc['Creative_set'] == 'set2') & (dfcopydoc['Model'] == models_lut[model_index])]
		df.loc[(bmw_model & bmw_region & df728x90),'CTA_text'] = set2copy['Deal_copy'].values[0]
		df.loc[(bmw_model & bmw_region & df728x90),'is_active'] = set2copy['isActive'].values[0]
		df.loc[(bmw_model & bmw_region & df728x90),'weighting'] = int(set2copy['Weight'].values[0]) or 1
		df.loc[(bmw_model & bmw_region & df728x90),'exit_URL'] = dfUrl['Exit_url'].values[0]
		

		#set 3 - 160x600
		set3copy = dfcopydoc.loc[ (dfcopydoc['Region'] == regions_lut[region_index]) & (dfcopydoc['Creative_set'] == 'set3') & (dfcopydoc['Model'] == models_lut[model_index])]
		df.loc[(bmw_model & bmw_region & df160x600) ,'CTA_text'] = set3copy['Deal_copy'].values[0]
		df.loc[(bmw_model & bmw_region & df160x600) ,'is_active'] = set3copy['isActive'].values[0]
		df.loc[(bmw_model & bmw_region & df160x600) ,'weighting'] = int(set3copy['Weight'].values[0]) or 1
		df.loc[(bmw_model & bmw_region & df160x600) ,'exit_URL'] = dfUrl['Exit_url'].values[0]
		
		df.loc[dfWeight,'weighting'] = 1
# df1 = df['coverage'] > 50
# df[df1]['Pima'] = 123

# df.loc[(df2Series & dfBaltimore & df300x250) | (df2Series & dfBaltimore & df300x600) | (df2Series & dfBaltimore & df970x250),'CTA_text'] = dfcopydoc.loc[ (dfcopydoc['Region'] == 'Baltimore') & (dfcopydoc['Creative_set'] == 'set1') & (dfcopydoc['Model'] == 'two_series')]

today_timestamp = str(datetime.datetime.today()).split()[0] + "-" + str(datetime.datetime.today()).split()[1]

df.to_csv('../dataSources/east/BMW_EAST_dataFeedUpdate-'+today_timestamp+'.csv', sep=',')