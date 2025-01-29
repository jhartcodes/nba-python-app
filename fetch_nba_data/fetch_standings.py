from nba_api.stats.endpoints import LeagueStandings
import pandas as pd

def get_team_standings(season='2024-25', season_type='Regular Season'):
    """
    Fetches current NBA standings for the specified season and season type.
    """
    # Initialize the LeagueStandings endpoint
    standings = LeagueStandings(season=season, season_type=season_type).get_data_frames()[0]

    # Display available columns for reference
    print("Available columns:", standings.columns)

    # Select relevant columns
    standings_df = standings[['TeamID', 'TeamCity', 'TeamName', 'Conference', 'WINS', 'LOSSES', 'WinPCT', 'PlayoffRank']]

    return standings_df

def save_standings_to_csv(season='2024-25', season_type='Regular Season'):
    """
    Fetches standings and saves them to a CSV file.
    """
    standings_df = get_team_standings(season, season_type)
    standings_df.to_csv("data/nba_standings.csv", index=False)
    print("✅ NBA team standings saved!")

if __name__ == "__main__":
    save_standings_to_csv()
