const express = require('express')
const morgan = require('morgan')
const path = require('path')
const app = express()

app.use(morgan('dev'))
app.use(express.urlencoded({ extended: true }))
app.use(express.json())

const goalieRoutes = require('./routes/goalieRoutes')
const playerRoutes = require('./routes/playerRoutes')
const standingsRoutes = require('./routes/standingsRoutes')
const matchupRoutes = require('./routes/matchupRoutes')
const emailRoutes = require('./routes/emailRoutes')
const teamRoutes = require('./routes/teamRoutes')

app.use('/goalies', goalieRoutes)
app.use('/players', playerRoutes)
app.use('/standings', standingsRoutes)
app.use('/matchups', matchupRoutes)
app.use('/email', emailRoutes)
app.use('/teams', teamRoutes)

const filePath = path.join(__dirname, 'views')

app.get('/', (req, res) => {
  res.sendFile(filePath + '/welcome.html')
})

app.get('/email', (req, res) => {
  res.sendFile(filePath + '/email-sub.html')
})

module.exports = app
