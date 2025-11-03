from openai import OpenAI
from dotenv import load_dotenv
import json
import os


load_dotenv()

api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI(api_key=api_key) 


def get_game_descriptions(df):

  results_json = df.to_json(orient='records')
  rows = json.loads(results_json)

  results_list = []

  for row in rows:
      row_str = "\n".join(f"{k}: {v}" for k, v in row.items())
      input_text = f"You're a professional journalist. Write a quick summary of who beat who, less than 25 words:\n{row_str}"
      response = client.responses.create(
          model="gpt-4.1-nano", 
          input=input_text,
          max_output_tokens=150
      )
      results_list.append(response.output_text)
      
  return results_list    