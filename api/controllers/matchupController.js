const db = require('../config/db-config')

const getAllMatchups = (req, res) => {
  const sql = 'select * from matchups where '
  db.all(sql, (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        error: err,
      })
    }

    if (rows.length == 0) {
      return res.status(404).json({
        status: 'failed',
        error: 'Could not find any matchups',
      })
    }

    return res.status(200).send(rows)
  })
}

const getMatchupsByTeamId = (req, res) => {
  const team_id = req.params.id

  const sql = 'SELECT * from matchups where Home_Id = ? or Visitor_Id = ?'

  db.all(sql, [team_id, team_id], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    if (rows.length == 0) {
      return res.status(500).json({
        status: 'failed',
        message: 'No matchups with that ID',
      })
    }

    return res.status(200).send(rows)
  })
}

const getMatchupsByWeek = (req, res) => {
  const week = req.params.week

  const sql = 'SELECT * from matchups where Week_Number = ?'

  db.all(sql, [week], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    if (rows.length == 0) {
      return res.status(500).json({
        status: 'failed',
        message: 'No matchups from that week',
      })
    }

    return res.status(200).send(rows)
  })
}

const getTodaysMatchups = (req, res) => {
  const date = new Date()

  const formatted = date.toISOString().split('T')[0]

  const sql = 'select * from matchups where Date = ?'

  db.all(sql, [formatted], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    if (rows.length == 0) {
      return res.status(404).json({
        status: 'failed',
        message: 'No matchups found on that day',
      })
    }
    return res.status(200).send(rows)
  })
}

module.exports = {
  getAllMatchups,
  getMatchupsByTeamId,
  getMatchupsByWeek,
  getTodaysMatchups,
}
