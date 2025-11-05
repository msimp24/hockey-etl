NHL ETL
Hockey ETL API that scrapes NHL data, transforms the data and loads it into a database.

The API provides routing for players, goalies, standings and matchups as well as a daily email newsletter for emails subscribed with results from the day before.

|Production https://hockey-stats-api.duckdns.org
Local (Development) http://localhost:8888

Players
API endpoints that returns details of players in the NHL

GET
Get all players
/players/all
Returns all players in the NHL and their stats

Query Params
GET
Get player by player name
/players/player?name=sidney crosby
Return players by name

Query Params
name
sidney crosby
GET
Top point getters
/players/top-point-getters?limit=2
Returns top point getters

Use limit to filter the amount of players, default is 10

Query Params
limit
2
GET
Filter By Team
/players/team/1
Returns players based on their team_id

GET /players/team/1

GET
Top Goals
/players/top-goals?limit=5
Returns top goal scores

Use limit to filter the amount of players, default is 10

GET /players/top-goals

Query Params
limit
5
Goalies
API endpoints that returns details/stats of goalies in the NHL

GET
Get all Goalies
/goalies/all
Returns all goalies

Query Params
GET
Get goalies by name
/goalies/goalie?name=dustin
Returns goalies by query name

Query Params
name
dustin
GET
Get top save perctages
/goalies/top-save-percentage?limit=5
Returns goalies by save percentage

Query Params
limit
5
GET
Get goalies by team id
/goalies/get-goalies-by-team/6
Returns all goalies from a team by their ID

GET
Get top goalies by win
/goalies/top-goalie-wins?limit=4

Query Params
limit
4
Standings
Endpoints of league standings

GET
Get League Standings
/standings
Returns the standings of all teams together

GET
Get Division Standings
/standings/division/central
Get division by division name

Divisions are : metropolitan, atlantic, pacific, and central

GET
Get Conference Standings
/standings/conference/eastern
Returns conference standings

eastern or western

Matchups
NHL schedule and results data

GET
Get All Matchups
/matchups
Returns all NHL matchups

Query Params
Home
Toronto
Away
Ottawa
GET
Get matchups by week
/matchups/week/26
Returns matchups by week number

Weeks 1-26

GET
Get Matchups by day
/matchups/today
Get todays matchup

GET
Get matchups by Id
/matchups/team/2
Get matchup by team id
returns all home and away games

Email Newsletter
Return daily scores from the day before at 6am

POST
Add new email
/email/add-subscription
Adds a new user to the email newsletter

Body
raw (json)
json
{
"first_name":"Mark",
"last_name":"Simpson",
"email":"mark.simpson4@gmail.com"
}
GET
Get all email subscriptions
/email/get-subs
Returns all email subscriptions

GET
Unsubscribe from mailing list
/email/delete-sub/mark.simpson4@gmail.com
Unsubscribe from the mail list

param is email of user that wants to unsubscribe

Teams
NHL teams data

GET
Get all teams
/teams/all
Returns all the teams and their IDs

GET
Return team by id
/teams/1
Returns a team but their Id
