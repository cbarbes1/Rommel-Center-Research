var http = require('http');
var url = require('url');
var fs = require('fs');
var path = require('path');
var express = require('express');
var app = express();




http.createServer(function (req, res) {
  var q = url.parse(req.url, true);
  var filename = "." + q.pathname;
  var extname = path.extname(filename);
  var contentType = 'text/html';

  if (extname === '.css') {
    contentType = 'text/css';
  }
  if (extname === '.js') {
    contentType = 'text/javascript';
  }

  if (filename.charAt(filename-1)=='/'){
    filename += 'index.html';
  }

  fs.readFile(filename, function(err, data) {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      return res.end("404 Not Found");
    } 
    
    res.writeHead(200, {'Content-Type': contentType});
    res.write(data);
    return res.end();
  });
}).listen(6969);