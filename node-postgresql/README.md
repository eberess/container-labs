# Recette de développement Node.js + PostgreSQL

Cette recette Docker Compose fournit un environnement de développement local pour une application Node.js connectée à une base de données PostgreSQL. Elle est idéale pour créer des API robustes avec un modèle de données relationnel.

---

### 📦 Prérequis

* **Docker** et **Docker Compose** installés.

---

### 📂 Structure du projet

La recette est organisée de manière simple pour une prise en main rapide :

* **`compose.yaml`** : Fichier de configuration des services (`app` et `db`).
* **`.env`** : Fichier pour stocker les variables d'environnement (identifiants, ports).
* **`app/`** : Répertoire de l'application Node.js.
    * `app/Dockerfile` : Instructions pour la construction de l'image Docker de l'application.
    * `app/index.js` : Le code source de l'API Express, avec les routes.
    * `app/package.json` : Les dépendances du projet (`express`, `sequelize`, `pg`).
    * `app/models/` : Le dossier contenant les modèles de la base de données.
        * `index.js` : Gère la connexion et les relations entre les modèles.
        * `post.js` : Modèle Sequelize pour les articles de blog.
        * `comment.js` : Modèle Sequelize pour les commentaires.

---

### 🛠️ Personnalisation de l'environnement

Les variables d'environnement sont gérées dans le fichier `.env` pour une meilleure flexibilité et sécurité.

* **`PORT_APP`** : Le port sur lequel l'application Node.js s'exécute (par défaut, `3001`).
* **`DB_USER`** : Utilisateur pour la connexion à la base de données.
* **`DB_PASS`** : Mot de passe de l'utilisateur.
* **`DB_NAME`** : Nom de la base de données.
* **`DB_HOST`** : Nom du service de la base de données (`db` par défaut).

---

### 🚀 Lancer l'environnement

1.  **Créez le fichier `.env`** et ajoutez-y vos variables d'environnement.
2.  **Lancez les conteneurs** en utilisant la commande Docker Compose :
    ```sh
    docker compose up -d --build
    ```
    Votre application sera accessible via `http://localhost:3001`.

---

### 🌐 Utilisation de l'API

Une fois les conteneurs démarrés, vous pouvez interagir avec l'API en utilisant **cURL** ou **Postman**.

#### Routes pour les articles (`/posts`)

* **Créer un article (POST)**
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Mon premier article", "content": "Contenu de mon article."}' http://localhost:3001/posts
    ```

* **Récupérer tous les articles (GET)**
    ```sh
    curl http://localhost:3001/posts
    ```

* **Récupérer un article par ID (GET)**
    ```sh
    curl http://localhost:3001/posts/1
    ```

* **Mettre à jour un article par ID (PUT)**
    ```sh
    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Titre mis à jour"}' http://localhost:3001/posts/1
    ```

* **Supprimer un article par ID (DELETE)**
    ```sh
    curl -X DELETE http://localhost:3001/posts/1
    ```

#### Routes pour les commentaires (`/posts/:postId/comments`)

* **Créer un commentaire (POST)**
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"content": "Super article !"}' http://localhost:3001/posts/1/comments
    ```

* **Récupérer les commentaires d'un article (GET)**
    ```sh
    curl http://localhost:3001/posts/1/comments
    ```

---

### 🛑 Arrêter et nettoyer

Pour arrêter les conteneurs et les réseaux, utilisez :
```sh
docker compose down
```
Pour supprimer également les volumes de données (par exemple, pour repartir avec une base de données vide), ajoutez l'option -v :
```sh
docker compose down -v
```
Cette commande est essentielle pour maintenir votre environnement de développement propre.

---
Si vous souhaitez en discuter ou si vous avez des questions, n'hésitez pas à me contacter par e-mail ou [LinkedIn](https://www.linkedin.com/in/el-beressa/). Je serais ravi d'échanger avec vous.
