
import pandas as pd
#csv file paths
TEAMPATH = "/Users/yasminesubbagh/Downloads/archive/teams.csv"
RANKINGPATH = "/Users/yasminesubbagh/Downloads/archive/ranking.csv"
GAMESPATH = "/Users/yasminesubbagh/Downloads/archive/games.csv"
GDPATH = "/Users/yasminesubbagh/Downloads/archive/games_details.csv"
PLAYERPATH = "/Users/yasminesubbagh/Downloads/archive/players.csv"

#read in the file
dfplayer = pd.read_csv(PLAYERPATH)
dfteam = pd.read_csv(TEAMPATH)
dfranking = pd.read_csv(RANKINGPATH)
dfgames = pd.read_csv(GAMESPATH)
dfgd = pd.read_csv(GDPATH)

#write back into the file
dfplayer.to_csv(PLAYERPATH, index=False)
print (dfplayer)
dfteam.to_csv(TEAMPATH, index=False)
print(dfteam)
dfranking.to_csv(RANKINGPATH, index=False)
print(dfranking)
dfgames.to_csv(GAMESPATH, index=False)
print(dfgames)
dfgd.to_csv(GDPATH, index=False)
print(dfgd)