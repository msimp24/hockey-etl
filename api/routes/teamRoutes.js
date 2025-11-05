const express = require('express')
const router = express.Router()

const { getAllTeams, getTeamByID } = require('../controllers/teamController')

router.route('/all').get(getAllTeams)

router.route('/:id').get(getTeamByID)

module.exports = router
