from utilities import *
import pandas as pd

file = "data/input/tactic.csv"
clean_df = Triplelift_Data().get_active_tactic(file)

failed_impression_data_object = pd.DataFrame(columns=['tactic','url'])
for index, row in clean_df.iterrows():
	impression_pixels = eval(row['impression_pixel_json']) #Cast string object as array object
	for impression_pixel in impression_pixels:
		clean_impression_pixel = impression_pixel.replace('\/','/') #replace all character occurrences of '\/' in URLs with '/'
		http_response = HTTP_Response(clean_impression_pixel)
		if http_response.is_ok():
			print(row['tactic_id'],clean_impression_pixel)
		if http_response.is_failed():
			failed_df = pd.DataFrame([[row['tactic_id'],clean_impression_pixel]],columns=['tactic','url'])
			failed_impression_data_object = failed_impression_data_object.append(failed_df)
failed_csv = "data/output/failed_impression_response_statuses.csv"
Triplelift_Data().save_tactic(failed_impression_data_object, failed_csv)
