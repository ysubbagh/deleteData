import pandas as pd
import numpy as np

#csv file path
GDPATH = "/Users/yasminesubbagh/Downloads/archive/games_details.csv"

#read in the file
df = pd.read_csv(GDPATH, dtype={'Column6': str}, low_memory=False)
#df.fillna(np.nan, inplace=True)

#ALTER the game details table
"""
df.drop('TEAM_ABBREVIATION', inplace=True, axis=1)
df.drop('TEAM_CITY', inplace=True, axis=1)
df.drop('PLAYER_NAME', inplace=True, axis=1)
df.drop('NICKNAME', inplace=True, axis=1)

df.columns = ['GameID', 'TeamID', 'PlayerID', 'StartPos', 'Comment', 'Minute', 'Field_Goals_Made', 'Field_Goals_Attempted', 'Field_Goal_Precent', '3Pt_Made', '3Pt_Attempted', '3Pt_Precent', 'Free_Throws_Made', 'Free_Throws_Attempted', 'Free_Throw_Precent', 'Offensive_Rebound', 'Defensive_Rebound', 'Total_Rebounds', 'Assists', 'Steals', 'Blocks', 'Turnovers', 'Personal_Fouls', 'Points', 'Plus_Minus']
"""

#fix all null minutes to be equal to -1

#output back into file, export
df.to_csv(GDPATH, index=False)
print(df)