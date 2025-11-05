🏒 Hockey Stats API Reference

This document provides a comprehensive reference for all endpoints available in the Hockey Stats API. All requests are served over HTTPS. The ETL process scrapes NHL data, transforms it, and loads it into the database daily at 6 AM.

🌐 Live Documentation & Postman Collection

For the most up-to-date and interactive documentation, including example responses and the ability to Fork the collection directly, please visit our https://documenter.getpostman.com/view/27229859/2sB3Wqv12F

Base URL

Component

Value

Production

https://hockey-stats-api.duckdns.org

Local (Development)

http://localhost:8888

🥅 Player Statistics Endpoints

Retrieves details and stats for NHL players.

Method

Path

Description

Example Path

GET

/players/all

Returns all players in the NHL and their statistics.

/players/all

GET

/players/player

Search for players by name.

/players/player?name=sidney%20crosby

GET

/players/top-point-getters

Returns top point getters. Default limit is 10.

/players/top-point-getters?limit=2

GET

/players/team/:team_id

Returns all players on a team specified by its ID.

/players/team/1

GET

/players/top-goals

Returns top goal scorers. Default limit is 10.

/players/top-goals?limit=5

Query Parameters:
| Parameter | Endpoints | Description | Example |
| :--- | :--- | :--- | :--- |
| name | /players/player | The name or partial name of the player. | sidney crosby |
| limit | /players/top-point-getters, /players/top-goals | Use to filter the amount of players returned (default 10). | 2 |

🧤 Goalie Statistics Endpoints

Retrieves details and statistics for NHL goalies.

Method

Path

Description

Example Path

GET

/goalies/all

Returns all goalies and their statistics.

/goalies/all

GET

/goalies/goalie

Search for goalies by name.

/goalies/goalie?name=dustin

GET

/goalies/top-save-percentage

Returns goalies sorted by top save percentage.

/goalies/top-save-percentage?limit=5

GET

/goalies/get-goalies-by-team/:team_id

Returns all goalies from a team by their ID.

/goalies/get-goalies-by-team/6

GET

/goalies/top-goalie-wins

Returns top goalies by win count.

/goalies/top-goalie-wins?limit=4

Query Parameters:
| Parameter | Endpoints | Description | Example |
| :--- | :--- | :--- | :--- |
| name | /goalies/goalie | The name or partial name of the goalie. | dustin |
| limit | /goalies/top-save-percentage, /goalies/top-goalie-wins | Use to filter the amount of goalies returned (default 10). | 5 |

📊 Standings Endpoints

Retrieves league and division standings.

Method

Path

Description

Example Path

GET

/standings

Returns the standings of all teams together (league-wide).

/standings

GET

/standings/division/:division_name

Get standings by division name.

/standings/division/central

GET

/standings/conference/:conference_name

Returns conference standings.

/standings/conference/eastern

Path Parameters:

:division_name: metropolitan, atlantic, pacific, or central.

:conference_name: eastern or western.

⚔️ Matchups & Schedule Endpoints

Retrieves NHL schedule and results data.

Method

Path

Description

Example Path

GET

/matchups

Returns all NHL matchups. Can be filtered by home and away query params.

/matchups?home=Toronto&away=Ottawa

GET

/matchups/week/:week_number

Returns matchups by week number (1-26).

/matchups/week/26

GET

/matchups/today

Get today's matchups.

/matchups/today

GET

/matchups/team/:team_id

Get matchups by team ID; returns all home and away games.

/matchups/team/2

📧 Email Subscription & Newsletter Endpoints

Manages user subscriptions and access to mailing list data.

Method

Path

Description

Example Path

POST

/email/add-subscription

Adds a new user to the daily email newsletter list.

/email/add-subscription

GET

/email/get-subs

Returns all email subscriptions (for administrative use).

/email/get-subs

GET

/email/delete-sub/:email

Unsubscribe a user from the mailing list. The parameter is the user's email.

/email/delete-sub/mark.simpson4@gmail.com

Request Body (POST /email/add-subscription):
The body must be sent as JSON:

{
"first_name": "Mark",
"last_name": "Simpson",
"email": "mark.simpson4@gmail.com"
}

🏒 Team Data Endpoints

Retrieves basic NHL team information.

Method

Path

Description

Example Path

GET

/teams/all

Returns all the NHL teams and their corresponding IDs.

/teams/all

GET

/teams/:team_id

Returns a specific team by its ID.

/teams/1
