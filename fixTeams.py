import pandas as pd
#csv file path
TEAMPATH = "/Users/yasminesubbagh/Downloads/archive/teams.csv"

#read in file
dfteam = pd.read_csv(TEAMPATH)

#ALTER file
dfteam.drop('LEAGUE_ID', inplace=True, axis=1)
dfteam.drop('ARENACAPACITY', inplace=True, axis=1)
dfteam.drop('DLEAGUEAFFILIATION', inplace=True, axis=1)

dfteam.columns = ['ID', 'Min_Yr', 'Max_Yr', 'Abbr', 'Nickname', 'Found_Year', 'City', 'Arena', 'Ownner', 'GM', 'Headcoach']

#export out
dfteam.to_csv(TEAMPATH, index=False)
print(dfteam)