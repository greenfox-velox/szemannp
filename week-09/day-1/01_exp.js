var express = require('express');
var http = require('http');
var app = express();

var date = new Date();
var currentTime = date.getHours() + ':' + date.getMinutes();

app.get('*', function(req, res) {
  res.send('request type: ' + req.method + '<br>' + 'req path: ' + req.path + '<br>' + 'date: ' + currentTime);
});

app.listen(3000);
