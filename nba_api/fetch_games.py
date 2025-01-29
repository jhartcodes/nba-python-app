from nba_api.stats.endpoints import Scoreboard
import datetime
import pandas as pd

def get_upcoming_games():
    """Fetches today's NBA games and returns as a DataFrame."""
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    games = Scoreboard(game_date=today).get_data_frames()[0]
    return games[['GAME_ID', 'GAME_DATE_EST', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'HOME_TEAM_WINS']]
