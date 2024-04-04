var http = require('http');
var url = require('url');
var fs = require('fs');
var express = require('express');
var app = express();

//app.use(express.static('style'));

http.createServer(function (req, res) {
  var q = url.parse(req.url, true);
  var filename = "." + q.pathname;

 // if (!fs.statSync(filename).isDirectory()) {
  fs.readFile(filename, function(err, data) {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      return res.end("404 Not Found");
    } 
    
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
//}
}).listen(6969);