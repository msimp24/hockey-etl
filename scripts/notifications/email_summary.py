import os
import resend
import datetime
import time
from dotenv import load_dotenv

from scripts.transform import transform_matchups
from scripts.ai.game_summaries import get_game_descriptions
from scripts.sql.get_subscriptions import get_subscriptions_data


load_dotenv()
api_key = os.environ.get('RESEND_API_KEY')
current_url = os.environ.get('CURRENT_URL')

if not api_key:
    raise ValueError("RESEND_API_KEY not set in environment variables")

resend.api_key = api_key


def send_email():

    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('%Y-%m-%d')

    matchups_df = transform_matchups()
    
    df = matchups_df[['Date', 'Time', 'Visitor', 'Visitor_Goals', 'Home', 'Home_Goals', 'Extra_Time', 'Attendance', 'Game_Duration']]

    todays_results = df[df['Date'] == yesterday ]
    
    game_descriptions = get_game_descriptions(todays_results)
    
    html_table = todays_results.to_html(index=False) 
    
    game_descriptions_html = ""
    
    for index, desc in enumerate(game_descriptions):
        game_descriptions_html += f"<p>Game {index+1}: {desc}</p>\n"


    subs = get_subscriptions_data() 
    for sub in subs:
        email_body = f"""
        <html>
        <body>
            <h1>Hi {sub[1]} {sub[2]}</h1>
            <br><br>
            <p>Here the results from yesterday's matchups</p>
            {html_table}
            <br><br>
            {game_descriptions_html}
            <br><br><br>
            <a href="{current_url}/email/delete-sub/{sub[3]}">Click here to unsubscribe</a>
        </body>
        </html>
        """
            
        params: resend.Emails.SendParams = {
            "from": "Hockey Data <noreply@mark-simpson.com>",
            "to": [sub[3]],
            "subject": "Hockey results",
            "html": email_body,
        }

        resend.Emails.send(params)
        time.sleep(0.6)

if __name__ == "__main__":
    send_email()        




