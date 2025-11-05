const db = require('../config/db-config')

const getAllPlayers = (req, res) => {
  const sql = `SELECT p.*, t.team_name from players as p join teams t on p.team_id = t.id `

  db.all(sql, (err, rows) => {
    if (err) {
      console.error('Database Query Failed:', err.message, err.code)
      return res.status(500).send({
        status: 'failed',
        error_code: err.code, // e.g., 'SQLITE_ERROR'
        error_number: err.errno, // e.g., 1 (the generic code)
        message: 'Database query failed: ' + err.message,
      })
      // --- END IMPROVED ERROR HANDLING ---
    }
    return res.status(200).send(rows)
  })
}

const getPlayersByName = (req, res) => {
  const name = req.query.name

  const sql = `SELECT p.*, t.team_name from players as p join teams t on p.team_id = t.id where name_display like ?`

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

const getTopPointGetters = (req, res) => {
  const limit = req.query.limit || 10

  const sql =
    'SELECT p.*, t.team_name from players as p join teams t on p.team_id = t.id order by points desc limit ?'

  db.all(sql, [limit], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    return res.status(200).send(rows)
  })
}

const filterByTeam = (req, res) => {
  const team_id = req.params.id

  if (!team_id) {
    return res.status(409).json({
      status: 'failed',
      message: 'Missing required fields',
    })
  }

  const sql =
    'SELECT p.*, t.team_name from players as p join teams t on p.team_id = t.id where team_id = ?'

  db.all(sql, [team_id], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }
    if (rows.length == 0) {
      return res.status(404).json({
        status: 'failed',
        message: 'No players found with that team ID',
      })
    }

    return res.status(200).send(rows)
  })
}

const getTopGoals = (req, res) => {
  const limit = req.query.limit || 10

  const sql =
    'SELECT p.*, t.team_name from players as p join teams t on p.team_id = t.id order by goals desc limit ?'

  db.all(sql, [limit], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    return res.status(200).send(rows)
  })
}
const getTopAssists = (req, res) => {
  const limit = req.query.limit || 10

  const sql =
    'SELECT p.*, t.team_name from players as p join teams t on p.team_id = t.id order by assists desc limit ?'

  db.all(sql, [limit], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    return res.status(200).send(rows)
  })
}

module.exports = {
  getAllPlayers,
  getPlayersByName,
  getTopPointGetters,
  filterByTeam,
  getTopGoals,
  getTopAssists,
}
