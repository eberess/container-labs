# Recette de développement Node.js + MongoDB

Cette recette Docker Compose fournit un environnement de développement local pour une application Node.js connectée à une base de données MongoDB. Elle est conçue pour être une base de travail rapide et efficace.

---

### 📦 Prérequis

* **Docker** et **Docker Compose** installés.

---

### 📂 Structure du projet

La recette est organisée de manière simple pour une prise en main rapide :

* **`docker-compose.yml`** : Le fichier principal qui configure et orchestre les services `app` et `db`.
* **`.env`** : Un fichier pour stocker les variables d'environnement, comme les identifiants et les ports, afin de sécuriser et de rendre la configuration plus flexible.
* **`app/`** : Le répertoire de l'application Node.js.
    * `app/Dockerfile` : Les instructions pour construire l'image Docker de l'application.
    * `app/index.js` : Le code source de l'application Express et Mongoose.
    * `app/package.json` : Les métadonnées et les dépendances du projet Node.js.

---

### 🛠️ Personnalisation de l'environnement

Les variables d'environnement sont gérées dans le fichier `.env` pour une meilleure flexibilité et sécurité. Vous pouvez les ajuster selon vos besoins :

* **`PORT_APP`** : Le port sur lequel l'application Node.js s'exécute (par défaut, `3000`).
* **`DB_USER`** : L'utilisateur pour l'authentification à la base de données MongoDB.
* **`DB_PASS`** : Le mot de passe de cet utilisateur.
* **`DB_NAME`** : Le nom de la base de données utilisée par l'application.
* **`DB_HOST`** : Le nom du service de la base de données tel qu'il est défini dans `docker-compose.yml`.

---

### 🚀 Lancer l'environnement

1.  **Créez le fichier `.env`** et ajoutez-y vos variables d'environnement.
2.  **Lancez les conteneurs** en utilisant la commande Docker Compose :
    ```sh
    docker compose up -d --build
    ```
    L'option `--build` permet de s'assurer que l'image de l'application Node.js est bien reconstruite avec les dernières modifications du code.

Votre application sera accessible via `http://localhost:3000`.

---

### 🌐 Utilisation de l'API

Une fois les conteneurs démarrés, vous pouvez interagir avec l'API REST pour la liste de tâches en utilisant un client HTTP comme **cURL** ou **Postman**.

* **Vérifier que l'API est en ligne**
    ```sh
    curl http://localhost:3000/
    ```

* **Créer une nouvelle tâche**
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Apprendre Docker"}' http://localhost:3000/todos
    ```

* **Récupérer toutes les tâches**
    ```sh
    curl http://localhost:3000/todos
    ```

---

### 🛑 Arrêter et nettoyer

Pour arrêter les conteneurs et les réseaux, utilisez la commande suivante :
```sh
docker compose down
```
Si vous souhaitez également supprimer les volumes de données (par exemple, pour repartir avec une base de données vide), ajoutez l'option -v :
```sh
docker compose down -v
```
Cette commande est essentielle pour maintenir votre environnement de développement propre.

---
Ce dépôt est le reflet de ma passion pour la conteneurisation et le développement. Si vous souhaitez en discuter ou si vous avez des questions, n'hésitez pas à me contacter par e-mail ou [LinkedIn](https://www.linkedin.com/in/el-beressa/). Je serais ravi d'échanger avec vous.
