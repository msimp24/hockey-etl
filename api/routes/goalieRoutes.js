const express = require('express')
const {
  getAllGoalies,
  getGoalieByName,
  getTopGoaliesSavePct,
  getGoaliesByTeam,
  getTopGoalieWins,
} = require('../controllers/goaliesController')
const router = express.Router()

router.route('/all').get(getAllGoalies)

router.route('/goalie').get(getGoalieByName)

router.route('/top-save-percentage').get(getTopGoaliesSavePct)

router.route('/get-goalies-by-team/:id').get(getGoaliesByTeam)

router.route('/top-goalie-wins').get(getTopGoalieWins)

module.exports = router
