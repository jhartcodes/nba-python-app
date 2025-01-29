from fetch_nba_data.fetch_teams import save_teams_to_csv
from fetch_nba_data.fetch_standings import save_standings_to_csv
from fetch_nba_data.fetch_games import save_games_to_csv

def main():
    print("📡 Fetching NBA Data...")
    save_teams_to_csv()
    save_standings_to_csv()
    save_games_to_csv()  # Now fetching upcoming games
    print("✅ All data has been fetched and saved!")

if __name__ == "__main__":
    main()
