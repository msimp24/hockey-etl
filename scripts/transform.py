import pandas as pd
import numpy as np
import unicodedata



from scripts.extract import extract_matchup_data, extract_standings_data, extract_player_stats

nhl_teams = {
    1: "Anaheim Ducks",
    2: "Boston Bruins",
    3: "Buffalo Sabres",
    4: "Calgary Flames",
    5: "Carolina Hurricanes",
    6: "Chicago Blackhawks",
    7: "Colorado Avalanche",
    8: "Columbus Blue Jackets",
    9: "Dallas Stars",
    10: "Detroit Red Wings",
    11: "Edmonton Oilers",
    12: "Florida Panthers",
    13: "Los Angeles Kings",
    14: "Minnesota Wild",
    15: "Montreal Canadiens",
    16: "Nashville Predators",
    17: "New Jersey Devils",
    18: "New York Islanders",
    19: "New York Rangers",
    20: "Ottawa Senators",
    21: "Philadelphia Flyers",
    22: "Pittsburgh Penguins",
    23: "San Jose Sharks",
    24: "Seattle Kraken",
    25: "St. Louis Blues",
    26: "Tampa Bay Lightning",
    27: "Toronto Maple Leafs",
    28: "Utah Mammoth",
    29: "Vancouver Canucks",
    30: "Vegas Golden Knights",
    31: "Washington Capitals",
    32: "Winnipeg Jets"
}

nhl_team_ids = {v: k for k, v in nhl_teams.items()}



nhl_abbrs = {
    "ANA": 1,
    "BOS": 2,
    "BUF": 3,
    "CGY": 4,
    "CAR": 5,
    "CHI": 6,
    "COL": 7,
    "CBJ": 8,
    "DAL": 9,
    "DET": 10,
    "EDM": 11,
    "FLA": 12,
    "LAK": 13,
    "MIN": 14,
    "MTL": 15,
    "NSH": 16,
    "NJD": 17,
    "NYI": 18,
    "NYR": 19,
    "OTT": 20,
    "PHI": 21,
    "PIT": 22,
    "SJS": 23,
    "SEA": 24,
    "STL": 25,
    "TBL": 26,
    "TOR": 27,
    "UTA": 28,
    "VAN": 29,
    "VEG": 30,
    "WSH": 31,
    "WPG": 32
}


def normalize_text(text):
    return unicodedata.normalize('NFC', text)

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

#functions for players/goalies

def add_team_id(df):
  df["team_id"] = df["team_name_abbr"].map(nhl_abbrs).astype("Int64")
  df['name_disply'] = df['name_display'].apply(normalize_text)
  
  return df

def add_numeric_columns(df):
  df = df.apply(pd.to_numeric, errors='ignore')
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
  df = add_team_id(df)
  df = add_numeric_columns(df)
  return df

def transform_goalie_stats():
  url = 'https://www.hockey-reference.com/leagues/NHL_2026_goalies.html'
  df = extract_player_stats(url)
  df = add_team_id(df)
  df = add_numeric_columns(df)
  

  return df

if __name__ =="__main__":
  transform_player_stats()
  
