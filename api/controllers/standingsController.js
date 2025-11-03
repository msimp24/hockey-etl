const db = require('../config/db-config')

const getLeagueStandings = (req, res) => {
  const sql = 'Select * from standings order by points_pct desc'

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

const getDivisionStandings = (req, res) => {
  const division = req.params.division

  if (!division) {
    return res.status(409).json({
      status: 'failed',
      message: 'Missing division requirement',
    })
  }

  const sql =
    'select * from standings where Division = ? order by points_pct desc'

  db.all(sql, [division], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    if (rows.length == 0) {
      return res.status(404).json({
        status: 'failed',
        message: `No data found in division ${division}`,
      })
    }

    return res.status(200).send(rows)
  })
}

const getConferenceStandings = (req, res) => {
  const conference = req.params.conference

  if (!conference) {
    return res.status(409).json({
      status: 'failed',
      message: 'Missing required conference field',
    })
  }
  const sql =
    'select * from standings where Conference = ? order by points_pct desc'

  db.all(sql, [conference], (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    if (rows.length == 0) {
      return res.status(404).json({
        status: 'failed',
        message: `No data found in conference ${conference}`,
      })
    }

    return res.status(200).send(rows)
  })
}

module.exports = {
  getLeagueStandings,
  getDivisionStandings,
  getConferenceStandings,
}
