const db = require('../config/db-config')

const getAllTeams = (req, res) => {
  const sql = 'SELECT * from teams'

  db.all(sql, (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    return res.status(200).send(rows)
  })
}

const getTeamByID = (req, res) => {
  const team_id = req.params.id

  const sql = 'select * from teams where id = ?'

  if (!team_id) {
    return res.status(409).send('Missing required fields')
  }

  db.all(sql, [team_id], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    return res.status(200).send(rows)
  })
}

module.exports = { getAllTeams, getTeamByID }
