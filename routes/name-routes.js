const express = require('express');
const { addAppUser,
    getAllAppUsers,
    getAppUser,
    updateAppUser,
    deleteAppUser
} = require('../controllers/nameController');

const router = express.Router();

router.post('/name', addAppUser);
router.get('/names', getAllAppUsers);
router.get('/name/:id', getAppUser);
router.put('/name/:id', updateAppUser);
router.delete('/name/:id', deleteAppUser);



module.exports = {
    routes: router
}