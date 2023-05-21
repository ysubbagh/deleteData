
import pandas as pd
#csv file paths
TEAMPATH = "/Users/yasminesubbagh/Downloads/archive/teams.csv"
RANKINGPATH = "/Users/yasminesubbagh/Downloads/archive/ranking.csv"
GAMESPATH = "/Users/yasminesubbagh/Downloads/archive/games.csv"
GDPATH = "/Users/yasminesubbagh/Downloads/archive/games_details.csv"
PLAYERPATH = "/Users/yasminesubbagh/Downloads/archive/players.csv"

#read in the file
dfplayer = pd.read_csv(PLAYERPATH)
"""
dfteam = pd.read_csv(TEAMPATH)
dfranking = pd.read_csv(RANKINGPATH)
dfgames = pd.read_csv(GAMESPATH)
dfgd = pd.read_csv(GDPATH)
"""


#ALTER players file
dfplayer.columns = ['Name', 'TeamID', 'ID', 'Season']
grouped = dfplayer.groupby(['Name', 'TeamID', 'ID'])
dfplayer['Start_Yr'] = grouped['Season'].transform('min')
dfplayer['End_Yr'] = grouped['Season'].transform('max')
dfplayer.drop_duplicates(subset=['Name', 'ID', 'TeamID'], inplace=True)
dfplayer = dfplayer[['ID', 'Name', 'TeamID', 'Start_Yr', 'End_Yr']]

#write back into the file
dfplayer.to_csv(PLAYERPATH, index=False)
print (dfplayer)
"""
dfteam.to_csv(TEAMPATH, index=False)
print(dfteam)
dfranking.to_csv(RANKINGPATH, index=False)
print(dfranking)
dfgames.to_csv(GAMESPATH, index=False)
print(dfgames)
dfgd.to_csv(GDPATH, index=False)
print(dfgd)
"""