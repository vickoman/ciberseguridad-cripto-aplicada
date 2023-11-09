const express = require("express");
const expressWinston = require('express-winston');
const winston = require('winston')
const logger = require('./utils/logger.js');
const raiseError = require('./utils/error.js');

global.logger = logger;
global.raiseError = raiseError;

const app = express();
const PORT = process.env.PORT || 8080;

// Import routes
const usersRoute = require('./routes/v1/users.js');
//Use Json
app.use(express.json());

/**
 * Winston configuration
 */
app.use(expressWinston.logger({
    winstonInstance: logger, // Usa el logger en Express-Winston
    format: winston.format.combine(
        winston.format.timestamp(),
    //     winston.format.colorize(),
    //     winston.format.json(),
    //     winston.format.simple()
    ),
    meta: true,
    msg: 'HTTP {{req.method}} {{req.url}}',
    expressFormat: true,
    colorize: true,
    ignoreRoute: function (req, res) { return false; },
    statusLevels: false,
    level: function(req, res) {
        let level = "";
        if (res.statusCode >= 100) { level = "info"; }
        if (res.statusCode >= 400) { level = "warn"; }
        if (res.statusCode >=500) { level = "error"; }
        return level;
    },
    dynamicMeta: function (req, res) {
        // Personaliza los campos de la metadata según tus necesidades
        const meta = {
            timestamp: new Date().toISOString()
        };
        return meta;
      },
}));


/**
 * Main entrypoint
 */
app.get('/', (req, res) => {
    const response = {
        "message": "Esta es una API de prueba, para el modulo de Criptografia Aplicada UCACUE",
        "members": [
            {
                name: "Ximena Pacheco"
            },
            {
                name: "Robin Cordova"
            },
            {
                name: "Ivan S"
            },
            {
                name: "Victor Diaz"
            },
            {
                name: "Galo M"
            }
        ],
        "professor": {
            "name": "Ronadl Criollo"
        }
    };
    res.json(response);
});

// Routes
app.use('/v1/users', usersRoute);

/**
 * Manejador de errores simple
 */
app.use((err, req, res, next) => {
    res.status(err.statusCode).json({ success: false, message: err.message, stack: err.stack});
});

app.listen(PORT, (req, res) => {
    console.log(`La API esta escuchando en el puerto ${PORT}`);
})