const express = require('express')
const {
  addEmailSubscription,
  getEmailSubs,
  removeEmailSubscription,
} = require('../controllers/emailController')
const router = express.Router()

router.route('/add-subscription').post(addEmailSubscription)

router.route('/get-subs').get(getEmailSubs)

router.route('/delete-sub/:email').get(removeEmailSubscription)

module.exports = router
