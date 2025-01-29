from nba_api.stats.endpoints import scoreboardv2, LeagueStandings
import pandas as pd
from datetime import datetime

def get_upcoming_games(date=None):
    """
    Fetches upcoming NBA games for a given date.
    Default: Today's games.
    """
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')

    # NBA API expects MM/DD/YYYY format
    formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%Y')

    # Fetch game data
    scoreboard = scoreboardv2.ScoreboardV2(game_date=formatted_date)
    games = scoreboard.get_data_frames()[0]

    # Display available columns for reference
    print("Available columns in games DataFrame:", games.columns)

    # Select relevant columns
    games_df = games[['GAME_ID', 'GAME_DATE_EST', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID']]

    return games_df

def get_team_standings(season='2024-25', season_type='Regular Season'):
    """
    Fetches current NBA standings for the specified season and season type.
    """
    standings = LeagueStandings(season=season, season_type=season_type).get_data_frames()[0]
    standings_df = standings[['TeamID', 'TeamCity', 'TeamName', 'Conference', 'WINS', 'LOSSES', 'WinPCT', 'PlayoffRank']]
    return standings_df

def save_games_to_csv(date=None):
    """
    Fetches upcoming NBA games and saves them to a CSV file.
    """
    games_df = get_upcoming_games(date)
    standings_df = get_team_standings()

    # Merge game data with standings
    games_with_standings = games_df.merge(standings_df, left_on='HOME_TEAM_ID', right_on='TeamID', suffixes=('_home', '_visitor'))
    games_with_standings = games_with_standings.merge(standings_df, left_on='VISITOR_TEAM_ID', right_on='TeamID', suffixes=('_home', '_visitor'))

    games_with_standings.to_csv("data/nba_upcoming_games_with_standings.csv", index=False)
    print(f"✅ NBA upcoming games with standings saved for {date or 'today'}!")

if __name__ == "__main__":
    save_games_to_csv()