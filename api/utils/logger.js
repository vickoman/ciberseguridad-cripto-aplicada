const winston = require("winston");
const LokiTransport = require("winston-loki");
const logger = winston.createLogger();

logger.add(
    new winston.transports.Console({
        format: winston.format.timestamp(),
    }),
);

// Add loki
logger.add(
    new LokiTransport({
        host: "http://127.0.0.1:3100",
        labels: { job: 'api-app' },
        json: true
    })
);
// const options = {
//     transports: [
//         new LokiTransport({
//             host: "http://127.0.0.1:3100",
//             labels: { job: 'api-app' },
//             json: true
//         }),
//         new transports.Console(),
//     ],
// };
module.exports = logger;
