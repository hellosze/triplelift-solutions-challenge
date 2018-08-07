from utilities import *

file = 'data/input/tactic.csv'
clean_df = Triplelift_Data().get_active_tactic(file)
print(clean_df)