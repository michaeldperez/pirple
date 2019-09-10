const http  = require('http');
const url   = require('url');

const requestHandler = (req, res) => {

};

const server = http.createServer(requestHandler);

server.listen(4000, () => {
    console.log('Server listening on port 4000');
});
