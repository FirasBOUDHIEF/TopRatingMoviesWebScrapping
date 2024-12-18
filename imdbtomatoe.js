const mongoose = require('mongoose');

const schemaTopMovie = mongoose.Schema({
    _id: String,
    Title: { type: String, required: true },
    Year: { type: String, required: true },
    Director: { type: String, required: true },
    Writers: { type: String, required: true },
    Actors: { type: String, required: true },
    Genre: { type: String, required: true },
    IMDbRating: { type: String, required: true },
    RottenTomatoes: { type: String, required: true },
});

const TopImdbTomatoe = mongoose.model('film', schemaTopMovie);

// Fonction pour récupérer tous les films
exports.getAllimdbTomatoes = () => {
    return new Promise((resolve, reject) => {
        mongoose.connect('mongodb://127.0.0.1:27017/scrapping')
            .then(() => TopImdbTomatoe.find({}).sort({ IMDbRating: -1 }))  // Tri par IMDbRating
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
