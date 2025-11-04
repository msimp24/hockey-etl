const express = require('express')
const morgan = require('morgan')
const app = express()

app.use(morgan('dev'))
app.use(express.json())

const goalieRoutes = require('./api/routes/goalieRoutes')
const playerRoutes = require('./api/routes/playerRoutes')
const standingsRoutes = require('./api/routes/standingsRoutes')
const matchupRoutes = require('./api/routes/matchupRoutes')
const emailRoutes = require('./api/routes/emailRoutes')

app.use('/goalies', goalieRoutes)
app.use('/players', playerRoutes)
app.use('/standings', standingsRoutes)
app.use('/matchups', matchupRoutes)
app.use('/email', emailRoutes)

module.exports = app
