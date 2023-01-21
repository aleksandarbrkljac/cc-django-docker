var express = require("express");
var router = express.Router();
const db = require("../repository");

router.post("/professors", db.createProfessor);
router.post("/students", db.createStudent);
module.exports = router;
