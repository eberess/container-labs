const express = require('express');
const mongoose = require('mongoose');

const app = express();
app.use(express.json());

// Variables d'environnement
const PORT = process.env.PORT_APP || 3000;
const DB_USER = process.env.DB_USER;
const DB_PASS = process.env.DB_PASS;
const DB_NAME = process.env.DB_NAME;
const DB_HOST = process.env.DB_HOST;

const MONGODB_URI = `mongodb://${DB_USER}:${DB_PASS}@${DB_HOST}:27017/${DB_NAME}`;

// Schéma de la tâche
const todoSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
    },
    completed: {
        type: Boolean,
        default: false,
    },
});

const Todo = mongoose.model('Todo', todoSchema);

// Connexion à la base de données
mongoose.connect(MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    authSource: 'admin'
})
.then(() => console.log('Connexion à MongoDB réussie'))
.catch(err => console.error('Erreur de connexion à MongoDB', err));

// Route POST pour créer une nouvelle tâche
app.post('/todos', async (req, res) => {
    try {
        const { title } = req.body;
        if (!title) {
            return res.status(400).send('Le titre est requis.');
        }
        const todo = new Todo({ title });
        await todo.save();
        res.status(201).send(todo);
    } catch (error) {
        res.status(500).send(error);
    }
});

app.get('/', (req, res) => {
    res.send('Bienvenue sur votre API de liste de tâches ! L\'API est prête.');
});

// Route GET pour récupérer toutes les tâches
app.get('/todos', async (req, res) => {
    try {
        const todos = await Todo.find();
        res.status(200).send(todos);
    } catch (error) {
        res.status(500).send(error);
    }
});

// Démarrer le serveur
app.listen(PORT, () => {
    console.log(`Le serveur écoute sur le port ${PORT}`);
});
