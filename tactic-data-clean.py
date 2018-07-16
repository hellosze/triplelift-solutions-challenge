import pandas as pd
import requests
import re

#import numpy as np

df = pd.read_csv('tactic.csv')
#print(df)
#clean_bool = (df['active'] == 1) & (df['deleted'] == 0) & ( (df['impression_pixel_json'] != '[]') | (df['impression_pixel_json'] != '') )
active_bool = df['active'] == 1
not_deleted_bool = df['deleted'] == 0
empty_array_bool = df['impression_pixel_json'] == '[]'
empty_string_bool = df['impression_pixel_json'].isnull()
#clean_bool = (df['active'] == 1) & (df['deleted'] == 0) & (df['impression_pixel_json'] != '[]') 
clean_bool = (active_bool & not_deleted_bool & ~empty_array_bool) & (active_bool & not_deleted_bool & ~empty_string_bool) 
#df2 = df['active'] == 1


clean_df = df[clean_bool]
# print(clean_df)
# print(len(df))
# print(len(clean_df))

#print(df2)

# clean_df.loc[:,'bloggg'] = 'dkfjldkjflkdajsflkdj'
# example of in place replacement

# clean_df.loc[~df['click_tracker_url'].isnull() & df['click_tracker_url'].str.startswith('https'),"secure_click"] = 1



def collect_http_response(url):
#def ping_impression(url):
	try:
		r = requests.get(url)
		if r.status_code >= 200 and r.status_code < 400:
			#print("Number OK")
			#print(r.status_code)
			return "Number OK"
		if r.status_code >= 400 and r.status_code < 600:
			#print("Number Failed")			
			return "Number Failed"
	except requests.exceptions.RequestException as e:
		# print(e)
			return "Number Failed"

collect_http_response('https://httpbin.org/status/404')
collect_http_response('http://www.google.com')
#print(r.json)

impression_pixel_tactics = []
impression_pixel_urls = []
impression_http_responses = []
for index, row in clean_df.iterrows():
	# print(row['tactic_id'])
	# print(row['impression_pixel_json'])
	impression_pixels = eval(row['impression_pixel_json'])
	for impression_pixel in impression_pixels:
		clean_impression_pixel = impression_pixel.replace('\/','/')
		# print(row['tactic_id'],clean_impression_pixel,collect_http_response(clean_impression_pixel))
		print(clean_impression_pixel)
		impression_pixel_tactics.append(row['tactic_id'])
		impression_pixel_urls.append(clean_impression_pixel)
		impression_http_responses.append(collect_http_response(clean_impression_pixel))

	# clean_impression_pixel = re.sub(r'\[\"','',row['impression_pixel_json']).replace('\/','/')

	#print(row['tactic_id'],clean_impression_pixel[0], len(clean_impression_pixel))
	# print(clean_impression_pixel[0])

impression_pixel_results_data = { 'tactic': impression_pixel_tactics, 
								'url': impression_pixel_urls, 
								'http_response': impression_http_responses
								}
impression_pixel_status_results = pd.DataFrame(impression_pixel_results_data, columns = ['tactic', 'url', 'http_response'])
impression_pixel_status_results.to_csv('impression_pixel_status.csv', sep=',')

