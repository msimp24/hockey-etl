const express = require('express')
const {
  getLeagueStandings,
  getConferenceStandings,
  getDivisionStandings,
} = require('../controllers/standingsController')
const router = express.Router()

router.route('/').get(getLeagueStandings)

router.route('/conference/:conference').get(getConferenceStandings)

router.route('/division/:division').get(getDivisionStandings)

module.exports = router
