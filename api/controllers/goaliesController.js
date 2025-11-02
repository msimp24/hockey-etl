const db = require('../config/db-config')

const getAllGoalies = (req, res) => {
  const sql = 'select * from goalies'

  db.all(sql, (err, rows) => {
    if (err) {
      return res.status(500).send({
        status: 'failed',
        message: err,
      })
    }
    return res.status(200).send(rows)
  })
}

const getGoalieByName = (req, res) => {
  const name = req.query.name

  const sql = `select * from goalies where name_display like ?`

  db.all(sql, [`%${name}%`], (err, rows) => {
    if (err) {
      return res.status(500).send({
        status: 'failed',
        message: err,
      })
    }
    return res.status(200).send(rows)
  })
}
const getTopGoaliesSavePct = (req, res) => {
  const limit = req.query.limit || 10

  const sql =
    'SELECT * from goalies where goalie_games > 2 order by save_pct_goalie desc limit ?'

  db.all(sql, [limit], (err, rows) => {
    if (err) {
      return res.status(500).send({
        status: 'failed',
        message: err,
      })
    }
    return res.status(200).send(rows)
  })
}

const getGoaliesByTeam = (req, res) => {
  const team_id = req.params.id

  const sql = 'SELECT * from goalies where team_id = ?'

  db.all(sql, [team_id], (err, rows) => {
    if (err) {
      return res.status(500).send({
        status: 'failed',
        message: err,
      })
    }
    return res.status(200).send(rows)
  })
}

const getTopGoalieWins = (req, res) => {
  const limit = req.query.limit || 10

  const sql = 'SELECT * from goalies order by goalie_wins desc limit ?'

  db.all(sql, [limit], (err, rows) => {
    if (err) {
      return res.status(500).send({
        status: 'failed',
        message: err,
      })
    }
    return res.status(200).send(rows)
  })
}

module.exports = {
  getAllGoalies,
  getGoalieByName,
  getTopGoaliesSavePct,
  getGoaliesByTeam,
  getTopGoalieWins,
}
