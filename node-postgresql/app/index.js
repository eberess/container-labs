const express = require('express');
const db = require('./models');

const app = express();
app.use(express.json());

const PORT = process.env.PORT_APP || 3001;
const Post = db.posts;
const Comment = db.comments;

// Démarrer le serveur et synchroniser la base de données
async function startServer() {
  try {
    await db.sequelize.authenticate();
    console.log('Connexion à PostgreSQL réussie.');

    await db.sequelize.sync({ alter: true });
    console.log('Modèles synchronisés avec la base de données.');

    // Routes de l'API
    app.get('/', (req, res) => {
      res.send('Bienvenue sur votre API de blog ! L\'API est prête.');
    });


    // Route pour créer un nouveau post
    app.post('/posts', async (req, res) => {
      try {
        const { title, content } = req.body;
        const post = await Post.create({ title, content });
        res.status(201).json(post);
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    });

    // Route pour récupérer tous les posts (avec leurs commentaires)
    app.get('/posts', async (req, res) => {
      try {
        const posts = await Post.findAll({
          include: [{ model: Comment }],
        });
        res.status(200).json(posts);
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    });

    // Route pour récupérer un post par son ID
    app.get('/posts/:postId', async (req, res) => {
      try {
        const post = await Post.findByPk(req.params.postId, {
          include: [{ model: Comment }],
        });
        if (!post) {
          return res.status(404).send('Post non trouvé.');
        }
        res.status(200).json(post);
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    });

    // Route pour mettre à jour un post
    app.put('/posts/:postId', async (req, res) => {
      try {
        const { title, content } = req.body;
        const post = await Post.findByPk(req.params.postId);
        if (!post) {
          return res.status(404).send('Post non trouvé.');
        }
        post.title = title || post.title;
        post.content = content || post.content;
        await post.save();
        res.status(200).json(post);
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    });

    // Route pour supprimer un post
    app.delete('/posts/:postId', async (req, res) => {
      try {
        const result = await Post.destroy({
          where: { id: req.params.postId },
        });
        if (result === 0) {
          return res.status(404).send('Post non trouvé.');
        }
        res.status(204).send(); // 204 No Content
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    });


    // Route pour créer un commentaire pour un post
    app.post('/posts/:postId/comments', async (req, res) => {
      try {
        const { content } = req.body;
        const post = await Post.findByPk(req.params.postId);
        if (!post) {
          return res.status(404).send('Post non trouvé.');
        }
        const comment = await Comment.create({
          content,
          PostId: post.id,
        });
        res.status(201).json(comment);
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    });

    // Route pour récupérer les commentaires d'un post
    app.get('/posts/:postId/comments', async (req, res) => {
      try {
        const post = await Post.findByPk(req.params.postId, {
          include: [{ model: Comment }],
        });
        if (!post) {
          return res.status(404).send('Post non trouvé.');
        }
        res.status(200).json(post.Comments);
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    });

    app.listen(PORT, () => {
      console.log(`Le serveur écoute sur le port ${PORT}`);
    });

  } catch (error) {
    console.error('Erreur de connexion à la base de données ou de synchronisation :', error);
  }
}

startServer();
