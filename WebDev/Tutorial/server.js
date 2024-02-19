//fileName: server.js
//Example using http module
const http= require('http');
//Create an HTTP server
const server=http.createServer((req,res)=>{
    //Set response headers
    res.writeHead(200,{'Content-Type': 'text/html'});
    //Write the response content
    res.write('<h1>Hello, Node.js HTTP Server! Its a miracle</h1>');
    res.end();
});
//Specify th eport to listen on
const port=3001;
//Start the Server
server.listen(port,() =>{
    console.log('Node.js HTTP server is running on port ${port}');
});
