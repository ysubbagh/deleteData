import pandas as pd
#csv file path
TEAMPATH = "/Users/yasminesubbagh/Downloads/archive/teams.csv"

#read in file
dfteam = pd.read_csv(TEAMPATH)

#ALTER file



#export out
dfteam.to_csv(TEAMPATH, index=False)
print(dfteam)