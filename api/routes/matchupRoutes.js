const express = require('express')
const {
  getAllMatchups,
  getMatchupsByTeamId,
  getMatchupsByWeek,
} = require('../controllers/matchupController')
const router = express.Router()

router.route('/').get(getAllMatchups)

router.route('/team/:id').get(getMatchupsByTeamId)

router.route('/week/:week').get(getMatchupsByWeek)
module.exports = router
