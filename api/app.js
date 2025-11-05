const express = require('express')
const morgan = require('morgan')
const app = express()

app.use(morgan('dev'))
app.use(express.json())

const goalieRoutes = require('./routes/goalieRoutes')
const playerRoutes = require('./routes/playerRoutes')
const standingsRoutes = require('./routes/standingsRoutes')
const matchupRoutes = require('./routes/matchupRoutes')
const emailRoutes = require('./routes/emailRoutes')

app.use('/goalies', goalieRoutes)
app.use('/players', playerRoutes)
app.use('/standings', standingsRoutes)
app.use('/matchups', matchupRoutes)
app.use('/email', emailRoutes)

module.exports = app
