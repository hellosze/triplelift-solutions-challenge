import pandas as pd
import re
import requests

class Triplelift_Data:
	def get_active_tactic_from_csv(self,file):
		df = pd.read_csv(file)
		active_bool = df['active'] == 1 #Select only Active Tactics
		not_deleted_bool = df['deleted'] == 0 #Select Tactics that have not been deleted
		empty_array_bool = df['impression_pixel_json'] == '[]' #Select Tactics that have empty arrays from the impression_pixel_json column
		empty_string_bool = df['impression_pixel_json'].isnull() #Select Tactics that are null from the impression_pixel_json column

		#logic to find active tactics that have not been deleted and have non-null impression pixels
		active_tactic_bool = (active_bool & not_deleted_bool & ~empty_array_bool) & (active_bool & not_deleted_bool & ~empty_string_bool) 
		return df[active_tactic_bool]
	def save_tactic(self,data_object,file):
		print(file)
		tactic_df = pd.DataFrame(data_object, columns = ['tactic', 'url'])
		tactic_df.to_csv(file, sep=',') #write http results to csv file

class HTTP_Response:
	def __init__(self,url):
		self.status = None
		#Method to check http status of URLs and group http status codes by OK and Failed.
		try:
			r = requests.get(url)
			if r.status_code >= 200 and r.status_code < 400: #buckdt all 2XX and 3XX responses as Number OK
				self.status = "OK"
			if r.status_code >= 400 and r.status_code < 600: #bucket all 4XX and 5XX responses as Number failed
				self.status = "Failed"
		except requests.exceptions.RequestException as e:
				self.status = "Failed"		
	def get_status(self):
		return self.status
	def is_ok(self):
		return self.status == "OK"
	def is_failed(self):
		return self.status == "Failed"


def test_is_failed():
	url_object = HTTP_Response("https://httpbin.org/status/404")
	assert url_object.is_failed() == True

def test_get_status():
	url_object = HTTP_Response("http://www.example.com")
	assert url_object.get_status() == "OK"

def test_is_ok():
	url_object = HTTP_Response("http://www.example.com")
	assert url_object.is_ok() == True

def test_HTTP_Response():
	url_object = HTTP_Response("http://www.example.com")
	assert url_object.status == "OK"

# url_object = HTTP_Response("http://www.example.com")
# print(url_object.status)

test_pd = Triplelift_Data().get_tactic("data/tests/test_tactic.csv")
print(test_pd)
pd2 = pd.DataFrame([[12187,333304,11600,28374,1,0,0,0,'https:\/\/www.example.com','https:\/\/www.example.com','https:\/\/www.example.com',0,'2/25/16 21:54']], columns = ['id','tactic_id','creative_library_id','creative_asset_id','active','deleted','click_tracker_url','click_tracker_encoding_level','impression_pixel_json','js_pixel_json','clickthrough_pixel_json','viewability_pixel_json','last_modified'])
print(pd2)
