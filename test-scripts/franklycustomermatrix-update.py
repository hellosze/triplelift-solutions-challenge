import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('franklycustomermatrix-v2.csv')
# df.set_index('unique_id', inplace=True)
#print(df[df['CTA_fontSize'] == '8px'])
# print(df)
websites = (df['Website'] != 'n/a')
print(df[websites])
# dfcopydoc = pd.read_csv('../dataSources/central/copydoc.csv')
# dfUrls = pd.read_csv('../dataSources/central/urls.csv')



# df300x600 = (df['dimension'] == '300x600')
# df300x250 = (df['dimension'] == '300x250')
# df970x250 = (df['dimension'] == '970x250')

# df728x90 = (df['dimension'] == '728x90')
# df160x600 = (df['dimension'] == '160x600')


# df300x50 = (df['dimension'] == '300x50')
# df320x50 = (df['dimension'] == '320x50')

# # dfAlbuquerque = (df['location'] == 'Albuquerque')
# # dfBakersfield = (df['location'] == 'Bakersfield')
# # dfBayArea = (df['location'] == 'Bay Area')
# # dfColoradoSprings = (df['location'] == 'Colorado Springs')
# # dfDenver = (df['location'] == 'Denver')
# # dfFresno = (df['location'] == 'Fresno')
# # dfHonolulu = (df['location'] == 'Honolulu')
# # dfLasVegas = (df['location'] == 'Las Vegas')
# # dfPhoenix = (df['location'] == 'Phoenix')
# # dfPortland = (df['location'] == 'Portland')
# # dfSacmod = (df['location'] == 'Sacmod')
# # dfSaltLake = (df['location'] == 'Salt Lake City')
# # dfSanDiego = (df['location'] == 'San Diego')
# # dfSLO = (df['location'] == 'San Luis Obispo')
# # dfSantaMaria = (df['location'] == 'Santa Maria')
# # dfSeattle = (df['location'] == 'Seattle')
# # dfSoCal = (df['location'] == 'SoCal')
# # baltimore = df[ (df['location'] == 'Baltimore') & (df['dimension'] != '320x50') & (df['dimension'] != '300x50')]

# # regions = [dfAlbuquerque,dfBakersfield,dfBayArea,dfColoradoSprings,dfDenver,dfFresno,dfHonolulu,dfLasVegas,dfPhoenix,dfPortland,dfSacmod,dfSaltLake,dfSanDiego,dfSeattle,dfSoCal]
# # regions_lut = ['Albuquerque', 'Bakersfield','Bay Area','Colorado Springs','Denver', 'Fresno','Honolulu', 'Las Vegas', 'Phoenix', 'Portland', 'Sacmod', 'Salt Lake City', 'San Diego', 'Seattle', 'SoCal']
# #regions = ['Albuquerque', 'Bakersfield','Bay Area','Colorado Springs','Denver', 'Fresno','Honolulu', 'Las Vegas', 'Phoenix', 'Portland', 'Sacmod', 'Salt Lake City', 'San Diego', 'Seattle', 'SoCal']
# regions = ['Cincinnati','Minneapolis','Columbus','Chicago','Cleveland','Dayton','Detroit','Pittsburgh','Kansas City','Indianapolis']

# # df2Series = (df['Model'] == 'two_series')
# # df3Series = (df['Model'] == 'three_series')
# # df4Series = (df['Model'] == 'four_series')
# # df4SeriesCoup = (df['Model'] == 'four_series_coup')
# # df5Series = (df['Model'] == 'five_series')
# # df6Series = (df['Model'] == 'six_series')
# # df7Series = (df['Model'] == 'seven_series')
# # dfi3Series = (df['Model'] == 'i3')
# # dfX1Series = (df['Model'] == 'X1')
# # dfX3Series = (df['Model'] == 'X3')
# # dfX4Series = (df['Model'] == 'X4')
# # dfX5Series = (df['Model'] == 'X5')
# # dfX6Series = (df['Model'] == 'X6')

# # models = [df2Series,df3Series,df4Series,df4SeriesCoup,df5Series,df6Series,df7Series,dfi3Series,dfX1Series,dfX3Series,dfX4Series,dfX5Series,dfX6Series]
# # models_lut = ["two_series", "three_series","four_series","four_series_coup","five_series","six_series","seven_series","i3","X1","X3","X4","X5","X6"]
# models = ["two_series", "three_series","four_series","four_series_coup","five_series","six_series","seven_series","i3","X1","X3","X4","X5","X6"]


# # print(baltimore)
# #print(df.dtypes.index)

# dfWeight = (df['weighting'] == 0)
# for region_index, bmw_region in enumerate(regions):
# 	for model_index, bmw_model in enumerate(models):
# 		dfLocalRegion = (df['location'] == bmw_region)
# 		dfLocalModel = (df['Model'] == bmw_model)
# 		dfUrl = dfUrls.loc[ (dfUrls['Region'] == bmw_region) & (dfUrls['Model'] == bmw_model)]
# 		print("/" + bmw_region + "/" + bmw_model)
# 		# print(dfUrl['Exit_url'].values[0] + "/" + regions_lut[region_index] + "/" + models_lut[model_index])

# 		# print(dfcopydoc.loc[ (dfcopydoc['Region'] == regions_lut[region_index]) & (dfcopydoc['Creative_set'] == 'set1') & (dfcopydoc['Model'] == models_lut[model_index])])
# 		#set 1 - 300x250, 300x600, 970x250
# 		set1copy = dfcopydoc.loc[ (dfcopydoc['Region'] == bmw_region) & (dfcopydoc['Creative_set'] == 'set1') & (dfcopydoc['Model'] == bmw_model)]
		
# 		df.loc[(dfLocalModel & dfLocalRegion & df300x250) | (dfLocalModel & dfLocalRegion & df300x600) | (dfLocalModel & dfLocalRegion & df970x250),'CTA_text'] = set1copy['Deal_copy'].values[0]
# 		#set1copy['Deal_copy'].values[0]
# 		df.loc[(dfLocalModel & dfLocalRegion & df300x250) | (dfLocalModel & dfLocalRegion & df300x600) | (dfLocalModel & dfLocalRegion & df970x250),'is_active'] = set1copy['isActive'].values[0]
# 		df.loc[(dfLocalModel & dfLocalRegion & df300x250) | (dfLocalModel & dfLocalRegion & df300x600) | (dfLocalModel & dfLocalRegion & df970x250),'weighting'] = int(set1copy['Weight'].values[0]) or 1
# 		df.loc[(dfLocalModel & dfLocalRegion & df300x250) | (dfLocalModel & dfLocalRegion & df300x600) | (dfLocalModel & dfLocalRegion & df970x250),'exit_URL'] = dfUrl['Exit_url'].values[0]
# 		df.loc[(dfLocalModel & dfLocalRegion & df300x50) | (dfLocalModel & dfLocalRegion & df320x50),'exit_URL'] = dfUrl['Exit_url'].values[0]

# 		#set 2 - 728x90
# 		set2copy = dfcopydoc.loc[ (dfcopydoc['Region'] == bmw_region) & (dfcopydoc['Creative_set'] == 'set2') & (dfcopydoc['Model'] == bmw_model)]
# 		df.loc[(dfLocalModel & dfLocalRegion & df728x90),'CTA_text'] = set2copy['Deal_copy'].values[0]
# 		df.loc[(dfLocalModel & dfLocalRegion & df728x90),'is_active'] = set2copy['isActive'].values[0]
# 		df.loc[(dfLocalModel & dfLocalRegion & df728x90),'weighting'] = int(set2copy['Weight'].values[0]) or 1
# 		df.loc[(dfLocalModel & dfLocalRegion & df728x90),'exit_URL'] = dfUrl['Exit_url'].values[0]
		

# 		#set 3 - 160x600
# 		set3copy = dfcopydoc.loc[ (dfcopydoc['Region'] == bmw_region) & (dfcopydoc['Creative_set'] == 'set3') & (dfcopydoc['Model'] == bmw_model)]
# 		df.loc[(dfLocalModel & dfLocalRegion & df160x600) ,'CTA_text'] = set3copy['Deal_copy'].values[0]
# 		df.loc[(dfLocalModel & dfLocalRegion & df160x600) ,'is_active'] = set3copy['isActive'].values[0]
# 		df.loc[(dfLocalModel & dfLocalRegion & df160x600) ,'weighting'] = int(set3copy['Weight'].values[0]) or 1
# 		df.loc[(dfLocalModel & dfLocalRegion & df160x600) ,'exit_URL'] = dfUrl['Exit_url'].values[0]
		
# 		df.loc[dfWeight,'weighting'] = 1

# today_timestamp = str(datetime.datetime.today()).split()[0] + "-" + str(datetime.datetime.today()).split()[1]
# df.to_csv('../dataSources/central/BMW_CENTRAL_dataFeedUpdate'+today_timestamp+'.csv', sep=',')

