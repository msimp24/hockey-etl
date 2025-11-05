const express = require('express')
const {
  getAllMatchups,
  getMatchupsByTeamId,
  getMatchupsByWeek,
  getTodaysMatchups,
} = require('../controllers/matchupController')
const router = express.Router()

router.route('/').get(getAllMatchups)

router.route('/team/:id').get(getMatchupsByTeamId)

router.route('/week/:week').get(getMatchupsByWeek)

router.route('/today').get(getTodaysMatchups)

module.exports = router
