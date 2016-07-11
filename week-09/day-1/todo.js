var express = require('express');
var bodyParser = require('body-parser');
var http = require('http');
var app = express();

var data = [
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    },
    {
        "completed": false,
        "id": 2,
        "text": "Make dinner"
    },
    {
        "completed": false,
        "id": 3,
        "text": "Save the world"
    }
];

app.use(bodyParser.json());
app.use(bodyParser.json({ type: 'application/*+json' }));
app.use(bodyParser.urlencoded({ extended: false }));


app.get('/todos', function(req, res) {
  res.send(data);
});


app.get('/todos/:id', function(req, res) {
  res.send(data.filter(function (item) {
    if (parseInt(item.id) === parseInt(req.params.id)) {
      return item;
    }
  }));
});

app.listen(3000);
