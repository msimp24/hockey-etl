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

app.use('/goalies', goalieRoutes)
app.use('/players', playerRoutes)
app.use('/standings', standingsRoutes)
app.use('/matchups', matchupRoutes)
app.use('/email', emailRoutes)

const filePath = path.join(__dirname, 'views')

app.get('/', (req, res) => {
  res.sendFile(filePath + '/welcome.html', (err) => {
    console.log('Error loading HTML file')
  })
})

app.get('/email', (req, res) => {
  res.sendFile(filePath + '/email-sub.html', (err) => {
    console.log('Error loading HTML file')
  })
})

module.exports = app
