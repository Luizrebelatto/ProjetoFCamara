'use strict';

const firebase = require('../db');
const Name = require('../models/name');
const db = firebase.firestore();


const addAppUser = async (req, res, next) => {
    try {
        const data = req.body;
        await db.collection('appUsers').doc().set(data);
        res.send('AppUser salvo com sucesso!');

    } catch (error) {
        res.status(400).send(error.message);
    }
}

const getAllAppUsers = async (req, res, next) => {
    try {
        const appUsers = await db.collection('appUsers');
        const data = await appUsers.get();
        const ARRappUsers = [];
        if (data.empty) {
            res.status(404).send('Not Found.');
        } else {
            data.forEach(doc => {
                const appUser = new Name(
                    doc.id,
                    doc.data().status,
                    doc.data().nomeResponsavel,
                    doc.data().nomeDependente,
                    doc.data().cidade,
                    doc.data().nomeEscola,
                    doc.data().contatoResponsavel,
                    doc.data().materialEscolar
                );
                ARRappUsers.push(appUser);

            });
            res.send(ARRappUsers);
        }
    } catch (error) {
        res.status(400).send(error.message);
    }
}

const getAppUser = async (req, res, next) => {
    try {
        const id = req.params.id;
        const appUsers = await db.collection('appUsers').doc(id)
        const data = await appUsers.get();
        if (!data.exists) {
            res.status(404).send('Not Found');
        } else {
            res.send(data.data());
        }

    } catch (error) {
        res.status(400).send(error.message);
    }
}

const updateAppUser = async (req, res, next) => {
    try {
        const id = req.params.id;
        const data = req.body;
        const appUser = await db.collection('appUsers').doc(id);
        await appUser.update(data);
        res.send('AppUser updated!');
    } catch (error) {
        res.status(400).send(error.message);
    }
}

const deleteAppUser = async (req, res, next) => {
    try {
        const id = req.params.id;
        await db.collection('appUsers').doc(id).delete();
        res.send('AppUser deleted!');
    } catch (error) {
        res.status(400).send(error.message);
    }
}


module.exports = {
    addAppUser,
    getAllAppUsers,
    getAppUser,
    updateAppUser,
    deleteAppUser
}