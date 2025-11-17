const express = require('express')
const morgan = require('morgan')
const path = require('path')
const app = express()
const expressLayouts = require('express-ejs-layouts')
const fs = require('fs')

app.use(expressLayouts)
app.use(express.static(path.join(__dirname, 'public')))
app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'ejs')

app.set('layout', 'layouts/layout')

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

const endpoints = path.join(__dirname, 'public', 'data', 'endpoints.json')

app.get('/', (req, res) => {
  const data = fs.readFileSync(endpoints, 'utf8')

  const jsonObject = JSON.parse(data)

  console.log(jsonObject)

  res.render('index', {
    players: jsonObject[0].endpoints,
    goalies: jsonObject[1].endpoints,
    standings: jsonObject[2].endpoints,
    matchups: jsonObject[3].endpoints,
    teams: jsonObject[5].endpoints,
    email: jsonObject[4].endpoints,
  })
})

app.get('/email', (req, res) => {
  res.render('email-sub')
})

app.get('/dashboard', (req, res) => {
  res.render('dashboard')
})

module.exports = app
