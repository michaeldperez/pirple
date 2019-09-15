const http              = require('http');
const url               = require('url');
const { StringDecoder } = require('string_decoder');

const handlers = {
    hello: (data, callback) => {
        callback(200, {message: 'Hello, World!'});
    },

    notFound: (data, callback) => {
        callback(404, null);
    },

    ping: (data, callback) => {
        callback(200, null);
    }
};

const router = {
    hello: handlers.hello,
    notfound: handlers.notFound,
    ping: handlers.ping
};

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

        const handler = typeof(router[trimmedPath]) !== 'undefined'
            ? router[trimmedPath]
            : router.notfound;

        const data = {
            headers,
            method,
            queryStr,
            payload,
            trimmedPath
        };

        handler(data, (statusCode, payload) => {
            statusCode == typeof(statusCode) === 'number'
                ? statusCode
                : 200;
            
            payload = typeof(payload) === 'object'
                ? payload
                : {};
            
            const serializedPayload = JSON.stringify(payload);

            res.setHeader('Content-Type', 'application/json');
            res.writeHead(statusCode);
            res.end(serializedPayload);

            console.log(`Returning response ${statusCode} and payload ${serializedPayload}`);
        });
    });
};

const server = http.createServer(requestHandler);

server.listen(4000, () => {
    console.log('Server listening on port 4000');
});
