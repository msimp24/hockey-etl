import os
import resend
import datetime
from dotenv import load_dotenv

from scripts.transform import transform_matchups
from scripts.ai.game_summaries import get_game_descriptions

load_dotenv()

api_key = os.environ.get('RESEND_API_KEY')

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


    email_body = f"""
    <html>
    <body>
        <p>Here are today's matchups:</p>
        {html_table}
        <br><br>
        {game_descriptions_html}
    </body>
    </html>
    """
    params: resend.Emails.SendParams = {
        "from": "Test <noreply@mark-simpson.com>",
        "to": ["mark.simpson4@gmail.com"],
        "subject": "Hockey results",
        "html": email_body,
    }

    email = resend.Emails.send(params)
    print(email)

if __name__ == "__main__":
    send_email()        




