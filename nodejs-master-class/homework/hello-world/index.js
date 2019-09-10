const http              = require('http');
const url               = require('url');
const { StringDecoder } = require('string_decoder');

const requestHandler = (req, res) => {
    let payload;
    const parsedUrl   = url.parse(req.url, true);
    const path        = parsedUrl.pathname;
    const queryStr    = parsedUrl.query;
    const trimmedPath = path.replace(/^\/+|\/+$/g, '');
    const method      = req.method.toUpperCase();
    const headers     = req.headers;
    const decoder     = new StringDecoder('utf-8');

    req.on('data', data => {
        payload += decoder.write(data);
    });

    req.on('end', () => {
        payload += decoder.end();
    });
};

const server = http.createServer(requestHandler);

server.listen(4000, () => {
    console.log('Server listening on port 4000');
});
