require('dotenv').config()

let express = require('express');
let app = express();

absolutePath = __dirname + "/views/index.html"
static = __dirname + "/public/"

app.use('/public', express.static(static))

app.use('/', function(req, res, next) {
  console.log(req.method + " " + req.url + " - " + req.ip);
  next();
})

app.get('/', function(req, res) {
  res.sendFile(absolutePath);
})

app.get('/json', function(req,res) {
  if (process.env.MESSAGE_STYLE == "uppercase") {
    res.json({"message": "HELLO JSON"});
  } else {
    res.json({"message": "Hello json"});
  }
})




































 module.exports = app;
