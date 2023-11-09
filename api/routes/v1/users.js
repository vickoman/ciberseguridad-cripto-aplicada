const express = require('express');
const router = express.Router();
const { users } = require('../../data.js');

const filterUserById = async (id) => {
    const user = users.filter((u) => u.id === id);
    return user;
}
router.get('/', (req, res, next) => {
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
})
module.exports = router;