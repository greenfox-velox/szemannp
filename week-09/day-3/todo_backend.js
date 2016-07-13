var express = require('express');
var bodyParser = require('body-parser');
var http = require('http');
var app = express();
var urlencodedParser = bodyParser.urlencoded({ extended: false });
var jsonParser = bodyParser.json();

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

function errorHandler(res, id) {
  if (id === undefined) {
    res.sendStatus(404);
  } else {
    res.send(id);
  }
}

app.use(bodyParser.json());
app.use(bodyParser.json({ type: 'application/*+json' }));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static('./static'));

app.get('/todos', function(req, res) {
  res.json(data);
});

app.get('/todos/:id', function(req, res) {
  res.json(data.filter(function (item) {
    if (parseInt(item.id) === parseInt(+req.params.id)) {
      return item;
    }
  }));
});

app.post('/todos', jsonParser, function(req, res) {
  var currentId = data.length;
  currentId++;
  var newTodo = {
    'completed': false,
    'id': currentId,
    'text': req.body.text
  };
  data.push(newTodo);
  res.send(newTodo);
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
