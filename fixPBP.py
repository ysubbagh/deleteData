#import packages
import pandas as pd

#path to file
PATH = '/Users/yasminesubbagh/Downloads/archive-3/csv/play_by_play.csv'

#read in the file
df = pd.read_csv(PATH)

#edit the file
df['pcttimestring'] = df['pcttimestring'].fillna(0)

#export / save the file
df.to_csv(PATH, index=False)
print (df)