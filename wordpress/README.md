# Recette pour WordPress

Cette recette fournit un environnement de développement local complet et portable pour les projets WordPress. Elle utilise Docker Compose pour orchestrer trois conteneurs : WordPress, une base de données MariaDB et un réseau personnalisé.

---

### 🚀 Fonctionnalités principales

* **Environnement isolé** : Crée un environnement de développement propre et reproductible.
* **Base de données persistante** : Les données de la base de données sont stockées sur la machine hôte pour ne pas être perdues.
* **Configuration flexible** : Utilise un fichier `.env` pour une configuration simple et sécurisée (ports, identifiants, etc.).
* **Gestion des limites d'upload** : Inclut un fichier `uploads.ini` pour ajuster les limites de téléchargement de PHP.

---

### 📦 Structure du projet

* `docker-compose.yml` : Le fichier de configuration principal.
* `.env` : Fichier de variables d'environnement.
* `html/` : Le dossier où les fichiers du cœur de WordPress seront téléchargés.
* `database/` : Le dossier où les données de la base de données seront persistées.
* `uploads.ini` : Fichier de configuration PHP.

---

### ⚙️ Comment lancer la recette

1.  **Copiez le fichier `.env`** et mettez à jour les variables avec vos propres valeurs.
2.  **Exécutez la commande** pour lancer l'environnement :
    ```sh
    docker-compose up -d
    ```
    Avec podman
    ```sh
    podman-compose up -d
    ```
3.  **Accédez à WordPress** : Une fois les conteneurs démarrés, ouvrez votre navigateur et allez à `http://localhost:8080` (ou le port que vous avez choisi).
