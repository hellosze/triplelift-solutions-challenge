import pandas as pd
import requests
import re


df = pd.read_csv('tactic.csv') #Read Triplelift Tactic Mapping in CSV Format into Pandas Dataframe object

active_bool = df['active'] == 1 #Select only Active Tactics
not_deleted_bool = df['deleted'] == 0 #Select Tactics that have not been deleted
empty_array_bool = df['impression_pixel_json'] == '[]' #Select Tactics that have empty arrays from the impression_pixel_json column
empty_string_bool = df['impression_pixel_json'].isnull() #Select Tactics that are null from the impression_pixel_json column

#logic to find active tactics that have not been deleted and have non-null impression pixels
clean_bool = (active_bool & not_deleted_bool & ~empty_array_bool) & (active_bool & not_deleted_bool & ~empty_string_bool) 
clean_df = df[clean_bool]



def collect_http_response(url):
#Method to check http status of URLs and group http status codes by OK and Failed.
	try:
		r = requests.get(url)
		if r.status_code >= 200 and r.status_code < 400: #buckdt all 2XX and 3XX responses as Number OK
			return "Number OK"
		if r.status_code >= 400 and r.status_code < 600: #bucket all 4XX and 5XX responses as Number failed
			return "Number Failed"
	except requests.exceptions.RequestException as e:
		# print(e)
			return "Number Failed"


#--------------
#for testing only
#collect_http_response('https://httpbin.org/status/404')
#collect_http_response('http://www.google.com')
#print(r.json)
#--------------


impression_pixel_tactics = []
impression_pixel_urls = []
impression_http_responses = []
for index, row in clean_df.iterrows():
	impression_pixels = eval(row['impression_pixel_json']) #Cast string object as array object
	for impression_pixel in impression_pixels:
		clean_impression_pixel = impression_pixel.replace('\/','/') #replace all character occurrences of '\/' in URLs with '/'
		
		print(clean_impression_pixel)
		
		impression_pixel_tactics.append(row['tactic_id'])
		impression_pixel_urls.append(clean_impression_pixel)
		impression_http_responses.append(collect_http_response(clean_impression_pixel))

impression_pixel_results_data = { 'tactic': impression_pixel_tactics, 
								'url': impression_pixel_urls, 
								'http_response': impression_http_responses
								}
impression_pixel_status_results = pd.DataFrame(impression_pixel_results_data, columns = ['tactic', 'url', 'http_response'])
impression_pixel_status_results.to_csv('impression_pixel_status-v2.csv', sep=',') #write http results to csv file

