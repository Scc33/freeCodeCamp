let express = require('express');
let app = express();

absolutePath = __dirname + "/views/index.html"
static = __dirname + "/public/"

app.use('/public', express.static(static))

app.get('/', function(req, res) {
  res.sendFile(absolutePath);
})

app.get('/json', function(req,res) {
  res.json({"message": "Hello json"});
})




































 module.exports = app;
