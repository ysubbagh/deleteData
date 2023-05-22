import pandas as pd

#csv file path
GDPATH = "/Users/yasminesubbagh/Downloads/archive/games_details.csv"

#read in the file
dfgd = pd.read_csv(GDPATH)

#ALTER the game details table
dfgd.drop('TEAM_ABBREVIATION', inplace=True, axis=1)
dfgd.drop('TEAM_CITY', inplace=True, axis=1)
dfgd.drop('PLAYER_NAME', inplace=True, axis=1)
dfgd.drop('NICKNAME', inplace=True, axis=1)
dfgd.drop('PLAYER_NAME', inplace=True, axis=1)

dfgd.columns = ['GameID', 'TeamID', 'PlayerID', 'StartPos', 'Comment', 'Minute', 'Field_Goals_Made', 'Field_Goals_Attemp', 'Field_Goal_Precent', '']

#output back into file, export
dfgd.to_csv(GDPATH, index=False)
print(dfgd)