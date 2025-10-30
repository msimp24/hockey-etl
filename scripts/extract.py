import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_data(url):
  req = requests.get(url)
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

