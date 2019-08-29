const http              = require('http');
const url               = require('url');
const { StringDecoder } = require('string_decoder');

const server = http.createServer((req, res) => {
    let buffer        = '';
    const parsedUrl   = url.parse(req.url, true);
    const path        = parsedUrl.pathname;
    const queryString = parsedUrl.query;
    const trimmedPath = path.replace(/^\/+|\/+$/g, '');
    const method      = req.method.toUpperCase();
    const headers     = req.headers;
    const decoder     = new StringDecoder('utf-8');

    req.on('data', data => {
        buffer += decoder.write(data);
    });

    req.on('end', () => {
        buffer += decoder.end();
        res.end('Hello World!\n');
        console.log(`${method} request received on path: ${trimmedPath}`);
        console.log('Query: ', queryString);
        console.log('Headers ', headers);
        console.log(`Payload: ${buffer}`);
    });

});

server.listen(3000, () => {
    console.log('The server is listening on port 3000');
});