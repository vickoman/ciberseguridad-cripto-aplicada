const express = require('express');
const fs = require('fs');
const router = express.Router();
const raiseError = require('../../utils/error.js');

const openDatabaseFile = async() => {
    const EntityDb = fs.readFileSync('db/usuarios.json', 'utf-8');
    const entity = JSON.parse(EntityDb);
    return entity;
}
const closeDatabaseFile = async(data) => {
    fs.writeFileSync('db/usuarios.json', JSON.stringify(data, null, 2), 'utf-8');
}

const filterUserById = async (id) => {
    const users = await openDatabaseFile();
    const user = users.filter((u) => u.id === id);
    return user;
}
const addUser = async (user) => {
    const users = await openDatabaseFile();
    users.push(user);
    await closeDatabaseFile(users);

    return user;
}
router.get('/', async(req, res, next) => {
    const users = await openDatabaseFile();
    if ( users ) {
        res.json({data: users})
    } else {
        next(raiseError(500, 'No existe la base de datos de usuarios'));
        next(error);
    }
});

router.get('/:id', async (req, res, next) => {
    const id = parseInt(req.params.id);

    if (id) {
        const userFound = await filterUserById(id);
        if (userFound.length === 0) {
            next(raiseError(404, `No existe usuario con el id #${id}`)); 
        } else {
            res.json({user: userFound[0]});
        }
    } else {
        next(raiseError(500, 'Se debe proporcionar el id numerico'));
    }
});

router.post('/new', async (req, res, next) => {
    const acceptProperties = ['id', 'nombres', 'apellidos', 'bio', 'edad'];
    // const {id, nombre } = req.body;
    const validateProperties =  acceptProperties.filter((p) => {
        const missinParameters = [];
        if (!req.body.hasOwnProperty(p)) {
            missinParameters.push(p);
            return missinParameters;
        }
    });
    if ( validateProperties.length > 0 ) {
        next(raiseError(400, `Faltan la informacion de ${validateProperties[0]} para ingresar el usuario`));
    } else {
        const u = await addUser(req.body);
        res.status(201).json({user: u});
    }
});

router.post('/error', async (req, res, next) => {
    next(raiseError(500, 'Error 500 Autogenerado'));
});
module.exports = router;