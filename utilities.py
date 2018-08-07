import pandas as pd
import re
import requests

class Triplelift_Data:
	def get_tactic(self,file):
		return pd.read_csv(file)
		#Read Triplelift Tactic Mapping in CSV Format into Pandas Dataframe object
	def get_active_tactic(self,file):
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
		# impression_pixel_status_results = pd.DataFrame(impression_pixel_results_data, columns = ['tactic', 'url', 'http_response'])
		# impression_pixel_status_results.to_csv('output/impression_pixel_status.csv', sep=',') #write http results to csv file
		tactic_df = pd.DataFrame(data_object, columns = ['tactic', 'url'])
		tactic_df.to_csv(file, sep=',') #write http results to csv file

		# return file

class HTTP_Response:
	def __init__(self,url):
		self.status = None
		#Method to check http status of URLs and group http status codes by OK and Failed.
		try:
			r = requests.get(url)
			if r.status_code >= 200 and r.status_code < 400: #buckdt all 2XX and 3XX responses as Number OK
				self.status = "OK"
				# return "Number OK"
			if r.status_code >= 400 and r.status_code < 600: #bucket all 4XX and 5XX responses as Number failed
				self.status = "Failed"
				# return "Number Failed"
		except requests.exceptions.RequestException as e:
			# print(e)
				self.status = "Failed"
				# return "Number Failed"		
	def get_status(self):
		return self.status
	def is_ok(self):
		return self.status == "OK"
	def is_failed(self):
		return self.status == "Failed"
