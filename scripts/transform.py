import pandas as pd
import numpy as np
from scripts.extract import extract_matchup_data, extract_standings_data, extract_player_stats

nhl_teams = {
    1: "Anaheim Ducks",
    2: "Arizona Coyotes",
    3: "Boston Bruins",
    4: "Buffalo Sabres",
    5: "Calgary Flames",
    6: "Carolina Hurricanes",
    7: "Chicago Blackhawks",
    8: "Colorado Avalanche",
    9: "Columbus Blue Jackets",
    10: "Dallas Stars",
    11: "Detroit Red Wings",
    12: "Edmonton Oilers",
    13: "Florida Panthers",
    14: "Los Angeles Kings",
    15: "Minnesota Wild",
    16: "Montreal Canadiens",
    17: "Nashville Predators",
    18: "New Jersey Devils",
    19: "New York Islanders",
    20: "New York Rangers",
    21: "Ottawa Senators",
    22: "Philadelphia Flyers",
    23: "Pittsburgh Penguins",
    24: "San Jose Sharks",
    25: "Seattle Kraken",
    26: "St. Louis Blues",
    27: "Tampa Bay Lightning",
    28: "Toronto Maple Leafs",
    29: "Utah Mammoth",
    30: "Vancouver Canucks",
    31: "Vegas Golden Knights",
    32: "Washington Capitals",
    33: "Winnipeg Jets"
}

nhl_team_ids = {v: k for k, v in nhl_teams.items()}


#matchups transform
def update_headers(df):
  new_headers = ['Game_Number', 'Date','Time', 'Visitor', 'Visitor_Goals', 'Home', 'Home_Goals', 'Extra_Time', 'Attendance', 'Game_Duration', 'Completed']
  df = df.set_axis(new_headers, axis=1)
  return df 

def add_week_column(df):
  season_start = pd.to_datetime("2025-10-06")
  df['Week_Number'] = ((pd.to_datetime(df['Date']) - season_start).dt.days // 7) + 1
  return df

def add_team_ids(df):
    df["Home_Id"] = df["Home"].map(nhl_team_ids).astype("Int64")
    df["Visitor_Id"] = df["Visitor"].map(nhl_team_ids).astype("Int64")  
    
    return df
  
def remove_whitespace(df):
  df = df.replace(
    to_replace=['', ' '], 
    value=np.nan)
  
  df['Completed'] = np.where(
    df['Visitor_Goals'].isna(),
    False,
    True
)
  return df


## Transforming Standing Data Frame


def transform_matchups():
  url = 'https://www.hockey-reference.com/leagues/NHL_2026_games.html'
  df = extract_matchup_data(url)
  df = update_headers(df)  
  df = remove_whitespace(df)
  df = add_week_column(df)
  df = add_team_ids(df)
  
  return df

def transform_standings():
  url = 'https://www.hockey-reference.com/leagues/NHL_2026_standings.html'
  df = extract_standings_data(url)
  return df
  
def transform_player_stats():
  url = 'https://www.hockey-reference.com/leagues/NHL_2026_skaters.html'
  df = extract_player_stats(url)
  return df

def transform_goalie_stats():
  url = 'https://www.hockey-reference.com/leagues/NHL_2026_goalies.html'
  df = extract_player_stats(url)
  return df


