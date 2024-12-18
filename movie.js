const mongoose = require('mongoose');

// Définition du schéma du film
const schemaTopMovie = mongoose.Schema({
    _id: String,
    Title: { type: String, required: true },
    IMDBRating: { type: String, required: true },
    Director: { type: String, required: true },
    Writer: { type: String, required: true },
    Actors: { type: String, required: true },
    Released: { type: String, required: true },
    Genre: { type: String, required: true },
});

// Modèle du film
const TopImdbTomatoe = mongoose.model('movie', schemaTopMovie);

// Fonction pour récupérer tous les films
exports.getAllMovies = () => {
    return new Promise((resolve, reject) => {
        mongoose.connect('mongodb://127.0.0.1:27017/scrapping')
            .then(() => TopImdbTomatoe.find({}).sort({ IMDBRating: -1 }))
            .then(movies => {
                mongoose.disconnect();
                resolve(movies);
            })
            .catch(err => {
                mongoose.disconnect();
                reject(err);
            });
    });
};
