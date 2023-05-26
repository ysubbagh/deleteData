
import pandas as pd
#csv file paths
TEAMPATH = "/Users/yasminesubbagh/Downloads/archive-2/teams.csv"

#read in the file
df = pd.read_csv(TEAMPATH)

#ALTER the teams csv to get stadiums
df.drop('LEAGUE_ID', inplace=True, axis=1)
df.drop('TEAM_ID', inplace=True, axis=1)
df.drop('MIN_YEAR', inplace=True, axis=1)
df.drop('MAX_YEAR', inplace=True, axis=1)
df.drop('ABBREVIATION', inplace=True, axis=1)
df.drop('NICKNAME', inplace=True, axis=1)
df.drop('YEARFOUNDED', inplace=True, axis=1)
df.drop('OWNER', inplace=True, axis=1)
df.drop('GENERALMANAGER', inplace=True, axis=1)
df.drop('HEADCOACH', inplace=True, axis=1)
df.drop('DLEAGUEAFFILIATION', inplace=True, axis=1)

df.columns = ['City', 'Arena', 'Arena_Capacity']

city_state_mapping = {
    'Atlanta': 'Georgia',
    'Boston': 'Massachesetts',
    'New Orleans': 'Louisiana',
    'Chicago': 'State3',
    'Dallas': 'Texas',
    'Denver': 'Colorado',
    'Houston': 'Texas',
    'Los Angeles': 'California',
    'Miami': 'Florida',
    'Milwaukee': 'Wisconsin',
    'Minneapolis': 'Minnesota',
    'Brooklyn': 'New York',
    'New York': 'New York',
    'Orlando': 'Florida',
    'Indianapolis': 'Indiana',
    'Philadelphia': 'Pennsylvania',
    'Phoneix': 'Arizona',
    'Portland': 'Oregon',
    'Sacramento': 'California',
    'San Antonio': 'California',
    'Oklahoma City': 'Oklahoma',
    'Toronto': 'Canada',
    'Salt Lake City': 'Utah',
    'Memphis': 'Tennessee',
    'Washington': 'Virginia',
    'Detroit': 'Michigan',
    'Charlotte': 'North Carolina',
    'Cleveland': 'Ohio',
    'San Francisco': 'California',
}

df['State'] = df['City'].map(city_state_mapping)
df['ID'] = df.groupby(level=0).cumcount()

#write back into the file
df.to_csv(TEAMPATH, index=False)
print(df)
