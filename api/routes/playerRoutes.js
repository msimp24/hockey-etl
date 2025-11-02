const express = require('express')
const {
  getAllPlayers,
  getPlayersByName,
  getTopPointGetters,
  filterByTeam,
  getTopGoals,
  getTopAssists,
} = require('../controllers/playerController')
const router = express.Router()

router.route('/all').get(getAllPlayers)

router.route('/player').get(getPlayersByName)

router.route('/top-point-getters').get(getTopPointGetters)

router.route('/top-goals').get(getTopGoals)

router.route('/top-assists').get(getTopAssists)

router.route('/team/:id').get(filterByTeam)

module.exports = router
