const express = require('express');
const path = require('path');
const app = express();

const doctorController=require('./controllers/movie')
const tomatoeController=require('./controllers/tomatoe')
const imdbtomatoeController=require('./controllers/imdbtomatoe')



// Importation du routeur des médecins
const RouterDoctor = require('./routers/movie');
const RouterTomatoe = require('./routers/tomatoe');
const RouterimdbTomatoe = require('./routers/imdbtomatoe');




// Middleware pour servir les fichiers statiques
app.use(express.static(path.join(__dirname, 'assets')));


// Configuration de EJS comme moteur de vue
app.set('view engine', 'ejs');
app.set('views', 'views');

// Utilisation du routeur pour la route '/'
app.use('/', RouterDoctor);


app.use('/', RouterTomatoe);

app.use('/', RouterimdbTomatoe);







// Démarrage du serveur
app.listen(3000, () => {
    console.log('Server is running on port 3001');
});
