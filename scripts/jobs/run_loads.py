# scripts/run_loads.py
from scripts.loads import goalie_load, matchup_load, player_load, standings_load
from scripts.notifications import email_summary

def run_all_loads():
  goalie_load.loadData()
  matchup_load.loadData()
  player_load.loadData()
  standings_load.loadData()
  #email_summary.send_email()
  

if __name__ == "__main__":
    run_all_loads()