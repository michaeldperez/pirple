const http                    = require('http');
const https                   = require('https');
const url                     = require('url');
const fs                      = require('fs');
const { StringDecoder }       = require('string_decoder');
const { httpPort, httpsPort } = require('./config');

const httpsOptions = {
    key: fs.readFileSync('./certs/key.pem'),
    cert: fs.readFileSync('./certs/cert.pem')
};
const httpServer   = http.createServer(unifiedServer);
const httpsServer  = https.createServer(httpsOptions, unifiedServer); 

httpServer.listen(httpPort, () => {
    console.log(`The http server is listening on port ${httpPort}`);
});

httpsServer.listen(httpsPort, () => {
    console.log(`The https server is listening on port ${httpsPort}`);
});

function unifiedServer(req, res) {
    let payload       = '';
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
};

const handlers = {
    ping: (data, callback) => {
        callback(200);
    },

    notFound: (data, callback) => {
        callback(404);
    }
};

const router = {
    ping: handlers.ping,
    notFound: handlers.notFound
};