from nba_api.fetch_teams import get_nba_teams, get_team_standings
from nba_api.fetch_games import get_upcoming_games

def main():
    # Fetch and display NBA teams
    teams_df = get_nba_teams()
    print("🏀 NBA Teams:\n", teams_df.head())

    # Fetch and display current team standings
    standings_df = get_team_standings()
    print("\n📊 Current Standings:\n", standings_df.head())

    # Fetch and display upcoming games
    games_df = get_upcoming_games()
    print("\n📅 Upcoming Games:\n", games_df.head())

if __name__ == "__main__":
    main()
