from nba_api.stats.static import teams

import pandas as pd

def get_nba_teams():
    nba_teams = teams.get_teams()
    return pd.DataFrame(nba_teams)

def save_teams_to_csv():
    teams_df = get_nba_teams()
    teams_df.to_csv("data/nba_teams.csv", index=False)
    print("✅ NBA teams saved!")

if __name__ == "__main__":
    save_teams_to_csv()
