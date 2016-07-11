var http = require('http');

var myServer = http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  var date = new Date();
  var currentTime = date.getHours() + ':' + date.getMinutes();
  res.end('path: ' + req.url + '\n\r' + 'with the method: ' + '\n\r' + req.method + currentTime);
});

myServer.listen(3000, '127.0.0.1');
