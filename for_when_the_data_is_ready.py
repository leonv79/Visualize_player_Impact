
import requests



#to find player team ids run these(there are also in separate files)




#Player_ID
#2023-24
from nba_api.stats.endpoints import LeagueDashPlayerShotLocations

# Set the season you're interested in
season = '2023-24'

# Create the API request
shot_locations = LeagueDashPlayerShotLocations(season=season)

# Retrieve the data
shot_locations_data = shot_locations.get_data_frames()[0]

import pandas as pd
# Extract only the player_id column
player_ids = shot_locations_data[[('', 'PLAYER_NAME'),('','PLAYER_ID')]]

# Display the player_ids
print(player_ids.head())



#Team_id
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

list_of_games = []

nba_teams = teams.get_teams()
team_ids = [team['id'] for team in nba_teams]

#find a player's id
player_id = player_ids[''][player_ids['']['PLAYER_NAME'] == 'Paul George']['PLAYER_ID'].values[0]

#find a team's id
# Example for Golden State Warriors
team_id = None
for team in nba_teams:
    if team['full_name'] == 'Los Angeles Clippers':
        team_id = team['id']
        break  # Stop once the team is found

print(team_id)


params = {
    "Season": "2023-24",
    "SeasonType": "Regular Season",
    "TeamId": team_id,
    #"Stat": stat_key,
    "PlayerId": player_id
}




url = "https://api.pbpstats.com/get-on-off/nba/player"

# Initialize an empty dictionary to store the DataFrames
dataframes = {}
import pickle
# To load the dictionary back
with open("pg_23_24.pkl", "rb") as f:
    loaded_dict = pickle.load(f)

#print(loaded_dict)
dataframes_3 = loaded_dict



   
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np 

pvalues = {}

# Perform the Wilcoxon signed-rank test for each DataFrame
for stat_key, df in dataframes_3.items():  ##
    if 'On' in df.columns and 'Off' in df.columns:
        # Perform the Wilcoxon signed-rank test
        # Convert 'On' and 'Off' to numeric values
        df['On'] = pd.to_numeric(df['On'])
        df['Off'] = pd.to_numeric(df['Off'])
        df = df[(df['MinutesOn']>150)&(df['MinutesOff']>150)]
        wilcoxon_test = stats.wilcoxon(df['On'], df['Off'])
        # Extract the p-value
        pvalue = wilcoxon_test.pvalue
        # Store the p-value in the dictionary
        pvalues[stat_key] = pvalue

# Convert the p-values dictionary to a DataFrame
pvalues_df = pd.DataFrame(list(pvalues.items()), columns=['Stat', 'P-Value'])

# Print the resulting DataFrame
print(pvalues_df)

for index, row in pvalues_df[pvalues_df['P-Value']<0.1].iterrows():
    # Access the P-Value in the row
    p_value = row['P-Value']
    stat_key = row['Stat']
    #find the player_name
    player_name = player_ids[''][player_ids['']['PLAYER_ID'] == pd.to_numeric(params['PlayerId'])]['PLAYER_NAME'].values[0]
    
    df = dataframes_3[stat_key]       ##
    df['On'] = pd.to_numeric(df['On'])
    df['Off'] = pd.to_numeric(df['Off'])
    df = df[(df['MinutesOn']>30)&(df['MinutesOff']>30)]
    mean_on = df['On'].mean()
    mean_off = df['Off'].mean()

    if mean_on > mean_off:
        print(f"The difference in {stat_key} is statistically significant, and {player_name} has a **positive impact** when he's on the game.")
    elif mean_on < mean_off:
        print(f"The difference in {stat_key} is statistically significant, but {player_name} has a **negative impact** when he's on the game.")
    else:
        print(f"The difference in {stat_key} is statistically significant, but {player_name}'s no notable change in performance.")

