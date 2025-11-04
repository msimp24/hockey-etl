const db = require('../config/db-config')
function isValidEmail(email) {
  const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/
  return emailRegex.test(email)
}

const addEmailSubscription = (req, res) => {
  const { first_name, last_name, email } = req.body

  if (!isValidEmail(email)) {
    return res.status(409).json({
      status: 'failed',
      message: 'Invalid email format',
    })
  }

  if (!first_name || !last_name || !email) {
    return res.status(409).json({
      status: 'failed',
      message: 'Missing required fields',
    })
  }

  const sql =
    'INSERT INTO subscriptions(first_name, last_name, email) values (?, ?, ?)'

  db.run(sql, [first_name, last_name, email], (err) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        err: err,
      })
    }

    return res.status(200).json({
      status: 'success',
      message: `${email} successfully added to daily subscriptions`,
    })
  })
}

const getEmailSubs = (req, res) => {
  const sql = 'SELECT * from subscriptions'

  db.all(sql, (err, rows) => {
    if (err) {
      return res.status(409).json({
        status: 'failed',
        message: err,
      })
    }

    return res.status(200).send(rows)
  })
}

const removeEmailSubscription = (req, res) => {
  const email = req.params.email

  if (!email) {
    return res.status(409).json({
      status: 'failed',
      messaga: 'Email is a required field',
    })
  }

  const sql = 'DELETE FROM subscriptions where email = ?'

  db.run(sql, [email], (err) => {
    if (err) {
      return res.status(500).json({
        status: 'failed',
        message: err,
      })
    }

    return res.status(200).json({
      status: 'success',
      message: `${email} successfully unsubscribed`,
    })
  })
}

module.exports = { addEmailSubscription, getEmailSubs, removeEmailSubscription }
