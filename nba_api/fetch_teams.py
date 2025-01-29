from nba_api.stats.static import teams
import pandas as pd

# Fetch all NBA teams
nba_teams = teams.get_teams()

# Convert to DataFrame for better readability
teams_df = pd.DataFrame(nba_teams)

# Select only relevant columns
teams_df = teams_df[['id', 'full_name', 'abbreviation', 'city', 'state', 'year_founded']]

teams_df.to_csv("data/nba_teams.csv", index=False)
print("✅ NBA teams saved!")


