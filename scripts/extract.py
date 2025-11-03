import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_matchup_data(url):
  req = requests.get(url)
  req.encoding = 'utf-8'
  req_html = req.text
  soup = BeautifulSoup(req_html, 'html.parser')
  filtered_trs = soup.select('tr:not(.thead):not(:first-child)')
  cleaned_rows = []

  for row in filtered_trs:
    cells = row.find_all(['th', 'td'])
    
    extracted_data = {}

    for cell in cells:
      key = cell.get('data-stat')
      value = cell.text.strip()
      extracted_data[key] = value
      
    cleaned_rows.append(extracted_data)
    

  df = pd.DataFrame.from_dict(cleaned_rows)
  df.insert(0, 'Game_Number', range(1, len(df) + 1))

  return df

def extract_standings_data(url):
  req= requests.get(url)
  req_html = req.text
  
  soup = BeautifulSoup(req_html, 'html.parser')
  east_table =soup.find("table", {"id": "standings_EAS"})
  east_table = east_table.find('tbody')
  
  west_table =soup.find("table", {"id": "standings_WES"})
  west_table = west_table.find('tbody')
  
  east_filtered_rows = east_table.select('tr:not(.thead)')
  west_filtered_rows = west_table.select('tr:not(.thead)')
    
  east_headers = east_table.find_all("tr", {"class":"thead"})
  west_headers = west_table.find_all("tr", {"class":"thead"})

  headers_rows = east_headers + west_headers
  
  divisions = []
  for row in headers_rows:
    text = row.get_text(strip=True)
    divisions.append(text)
    
  filtered_rows = east_filtered_rows + west_filtered_rows
  
  cleaned_data = []
  
  for row in filtered_rows:
    cells = row.find_all(['th', 'td'])
    
    extracted_data = {}
    
    for cell in cells:
      key = cell.get('data-stat')
      value = cell.text.strip()
      extracted_data[key] = value
    cleaned_data.append(extracted_data)  
    
    df = pd.DataFrame.from_dict(cleaned_data)
    df['Division'] = None
    df.loc[:7, 'Division'] = divisions[0][:-9]
    df.loc[8:15, 'Division'] = divisions[1][:-9]
    df.loc[16:23, 'Division'] = divisions[2][:-9]
    df.loc[24:31, 'Division'] = divisions[3][:-9]
    
  return df
  
def extract_player_stats(url):
  req = requests.get(url)
  req_html = req.text
  
  soup = BeautifulSoup(req_html, 'html.parser')
  
  data = soup.find('tbody')
  filtered_rows = data.find_all('tr')
  
  cleaned_data = []
  
  for row in filtered_rows:
    cells = row.find_all(['th', 'td'])
    
    extracted_data = {}
    
    for cell in cells:
      key = cell.get('data-stat')
      value = cell.text.strip()
      extracted_data[key] = value
    cleaned_data.append(extracted_data)  

  df = pd.DataFrame.from_dict(cleaned_data)
  return df


if __name__ == '__main__':
  extract_player_stats('https://www.hockey-reference.com/leagues/NHL_2026_skaters.html')