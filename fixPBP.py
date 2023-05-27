#import packages
import pandas as pd

#path to file
PATH = '/Users/yasminesubbagh/Downloads/archive-3/csv/play_by_play.csv'

#read in the file
df = pd.read_csv(PATH)

#edit the file
df['pctimestring'] = df['pctimestring'].fillna(0)
df.dropna(subset=['player1_id'], inplace=True)
df = df.drop(['wctimestring', 'video_available_flag', 'player1_name', 'player1_team_city', 'player1_team_nickname', 'player1_team_abbreviation', 'player2_name', 'player2_team_city', 'player2_team_nickname', 'player2_team_abbreviation', 'player3_name', 'player3_team_city', 'player3_team_nickname', 'player3_team_abbreviation'], axis=1)
df = df[df['player1_id'] != 1]

#export / save the file
df.to_csv(PATH, index=False)
print (df)