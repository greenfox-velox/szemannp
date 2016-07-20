'use strict';

var express = require('express');
var mysql = require('mysql');
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
var jsonParser = bodyParser.json();

var app = express();
var con = mysql.createConnection ({
  host: 'localhost',
  user: 'root',
  password: 'solar``7',
  database: 'todos'
});

function errorHandler(res, id) {
  if (id === undefined) {
    res.sendStatus(404);
  } else {
    res.send(id);
  }
};

var urlencodedParser = bodyParser.urlencoded({ extended: false });
var jsonParser = bodyParser.json();

app.use(express.static('public'));

app.use(jsonParser);
app.use(urlencodedParser);

con.connect(function (err) {
  if (err) {
    console.log('Error connecting to DataBase');
  }
  console.log('Connection established');
});

app.get('/todos/', function(req, res) {
  con.query('SELECT * FROM todos WHERE destroyed = "false"', function (err, data) {
    if (err) {
      console.log(err.toString());
    }
    console.log('Data recieved from DB:\n');
    console.log(data);
    res.json(data);
  });
});

app.get('/todos/:id', function(req, res) {
  con.query('SELECT * FROM todos WHERE id = ' + req.params.id, function (err, data) {
    if (err) {
      console.log(err.toString());
    }
    console.log('Data recieved from DB:\n');
    console.log(data);
    res.json(data[1]);
  });
});

app.post('/todos', function(req, res) {
  con.query('SELECT * FROM todos VALUES ("'+req.body.text+'")', function (err, data) {
    if (err) {
      console.log(err.toString());
    }
    res.json({id: data.insertId, text: req.body.text});
  });
});

app.put('/todos/:id', jsonParser, function (req, res) {
  var toPut = data.filter(function (item) {
    return item.id === +req.params.id;
  }) [0];
  toPut['completed'] = req.body['completed'];
  toPut['text'] = req.body['text'];
  res.json(toPut);
});

app.delete('/todos/:id', function(req, res) {
  res.json(data.filter(function (item) {
    if (item.id === +req.params.id) {
      item.destroyed = 'true';
      data.splice(data.indexOf(item), 1);
      return item;
    }
  })[0]);
});

app.listen(3000);
