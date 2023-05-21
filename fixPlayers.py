import pandas as pd
#csv file path
PLAYERPATH = "/Users/yasminesubbagh/Downloads/archive/players.csv"

#read in the file
dfplayer = pd.read_csv(PLAYERPATH)

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