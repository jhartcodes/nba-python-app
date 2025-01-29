from nba_api.stats.endpoints import teamgamelog
import pandas as pd
from fetch_nba_data.fetch_teams import get_nba_teams  # Import team IDs

def get_team_form():
    """
    Fetches last 10 games for each NBA team.
    """
    teams_df = get_nba_teams()  # Fetch team list
    team_ids = teams_df['id'].tolist()

    all_games = []

    for team_id in team_ids:
        gamelog = teamgamelog.TeamGameLog(team_id=team_id, season='2023-24').get_data_frames()[0]
        
        # Select only the last 10 games
        last_10_games = gamelog.head(10)
        
        # Add team ID column
        last_10_games['TEAM_ID'] = team_id
        all_games.append(last_10_games)

    # Merge all team logs into one DataFrame
    team_form_df = pd.concat(all_games)

    # Select relevant columns
    team_form_df = team_form_df[['TEAM_ID', 'Game_ID', 'Game_Date', 'WL', 'PTS', 'REB', 'AST']]

    return team_form_df

def save_team_form_to_csv():
    """
    Fetches team form (last 10 games) and saves it to CSV.
    """
    team_form_df = get_team_form()
    team_form_df.to_csv("data/nba_team_form.csv", index=False)
    print("✅ NBA team form saved!")

if __name__ == "__main__":
    save_team_form_to_csv()
