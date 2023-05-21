import pandas as pd
#csv file path
TEAMPATH = "/Users/yasminesubbagh/Downloads/archive/teams.csv"

#read in file
dfteam = pd.read_csv(TEAMPATH)

#ALTER file
#dfteam.drop('LEAGUE_ID', inplace=True, axis=1)
#dfplayer.columns = ['Name', 'TeamID', 'ID', 'Season']


#export out
dfteam.to_csv(TEAMPATH, index=False)
print(dfteam)