import pandas as pd

#csv file path
RANKINGPATH = "/Users/yasminesubbagh/Downloads/archive/ranking.csv"

#read in the file
dfranking = pd.read_csv(RANKINGPATH)

#ALTER ranking table
dfranking.drop('LEAGUE_ID', inplace=True, axis=1)
dfranking.drop('STANDINGSDATE', inplace=True, axis=1)
dfranking.drop('TEAM', inplace=True, axis=1)
dfranking.drop('HOME_RECORD', inplace=True, axis=1)
dfranking.drop('ROAD_RECORD', inplace=True, axis=1)
dfranking.drop('RETURNTOPLAY', inplace=True, axis=1)

dfranking.columns = ['TeamID', 'SeasonID', 'Confrence', 'Total_Games', 'Wins', 'Losses', 'Win_Percent']

inds_to_keep = dfranking.groupby(['TeamID', 'SeasonID'])['Total_Games'].idxmax()
dfranking = dfranking.loc[inds_to_keep]

dfranking = dfranking[dfranking['Total_Games'] != 0]

#export file out
dfranking.to_csv(RANKINGPATH, index=False)
print(dfranking)