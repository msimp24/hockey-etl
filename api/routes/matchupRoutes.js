const express = require('express')
const router = express.Router()

const getAllMatchups = (req, res) => {
  const sql = 'select * from matchups'

  db.all(sql, (err, rows) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        error: err,
      })
    }

    if (row.length == 0) {
      return res.status(404).json({
        status: 'failed',
        error: '',
      })
    }
  })
}

module.exports = router
