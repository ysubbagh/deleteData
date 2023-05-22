import pandas as pd

#csv file path
GAMESPATH = "/Users/yasminesubbagh/Downloads/archive/games.csv"

#read in the file
dfgames = pd.read_csv(GAMESPATH)

#ALTER the games table
dfgames.drop('GAME_STATUS_TEXT', inplace=True, axis=1)
dfgames.drop('TEAM_ID_home', inplace=True, axis=1)
dfgames.drop('TEAM_ID_away', inplace=True, axis=1)

dfgames.dropna(inplace=True)

dfgames.columns = ['Date', 'ID', 'HomeID', 'VisitorID', 'Season', 'Pts_H', 'FieldGoal_Perc_Home', 'Free_Throw_Home', '3Pt_Perc_Home', 'Assists_Home', 'Rebounds_Home', 'Points_Away', 'Field_Goals_Away', 'Free_Throw_Perc_Away', '3Pt_Perc_Away', 'Assists_Away', 'Rebound_Away', 'Home_Team_Wins']

#write back into the file, export
dfgames.to_csv(GAMESPATH, index=False)
print(dfgames)