const http              = require('http');
const url               = require('url');
const { StringDecoder } = require('string_decoder');
const { port, envName } = require('./config');

const server = http.createServer((req, res) => {
    let payload        = '';
    const parsedUrl   = url.parse(req.url, true);
    const path        = parsedUrl.pathname;
    const queryString = parsedUrl.query;
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
            : router.notFound;

        const data = {
            headers,
            method,
            queryString,
            payload,
            trimmedPath
        };

        handler(data, (statusCode, payload) => {
            statusCode = typeof(statusCode) === 'number'
                ? statusCode
                : 200;
            
            payload = typeof(payload) === 'object'
                ? payload
                : {};
            
            const serializedPayload = JSON.stringify(payload);

            res.setHeader('Content-Type', 'application/json');
            res.writeHead(statusCode);
            res.end(serializedPayload);

            console.log(`Returning response ${statusCode} and ${serializedPayload}`);
        });
    });

});

server.listen(3000, () => {
    console.log(`The server is listening on port ${port} in ${envName} mode`);
});

const handlers = {
    sample: (data, callback) => {
        callback(406, {'name': 'sample handler'});
    },

    notFound: (data, callback) => {
        callback(404);
    }
};

const router = {
    sample: handlers.sample,
    notFound: handlers.notFound
};