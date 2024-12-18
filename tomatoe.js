// models/tomatoe.js
const mongoose = require('mongoose');

const schemaTopMovie = mongoose.Schema({
    _id: String,
    Title: { type: String, required: true },
    Rating: { type: String, required: true },
});

const TopTomatoe = mongoose.model('tomatoe', schemaTopMovie);

// Fonction pour récupérer tous les films
exports.getAllTomatoes = () => {
    return new Promise((resolve, reject) => {
        mongoose.connect('mongodb://127.0.0.1:27017/scrapping')
            .then(() => TopTomatoe.find({}).sort({ Rating: -1 })) // Assurez-vous que vous utilisez TopTomatoe ici
            .then(movies => {
                mongoose.disconnect();
                resolve(movies);  // Retourner les films récupérés
            })
            .catch(err => {
                mongoose.disconnect();
                reject(err);
            });
    });
};
