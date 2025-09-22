# Projet de Gestion de Librairie-Bibliothèque 📚

Ce projet est une application full-stack de gestion de librairie-bibliothèque. Il se compose d'une API backend développée en Python avec le framework FastAPI et d'une application mobile en cours de développement avec Flutter. L'objectif est de gérer les prêts, les ventes, les stocks de livres, ainsi que les membres et les auteurs.

---

### Technologies Utilisées ⚙️

- **Backend** : Python 3.9, FastAPI
- **Base de Données** : PostgreSQL
- **Conteneurisation** : Docker, Docker Compose
- **Frontend** : Flutter (en cours de développement)

---

### Fonctionnalités de l'API 🚀

L'API REST permet de gérer les entités suivantes, avec une attention particulière à la gestion du stock et des transactions :

- **Livres** : Création, lecture par ID ou ISBN (code-barres), mise à jour et suppression.
- **Auteurs** : Création, lecture, mise à jour et suppression.
- **Membres** : Création, lecture, mise à jour et suppression.
- **Gestion des prêts** : Routes pour emprunter et rendre un livre via son ISBN. Ces routes mettent à jour le statut de disponibilité du livre.
- **Mode "Scan"** : L'API est optimisée pour la gestion en libre-service via un scanner de code-barres, permettant d'identifier rapidement un livre pour l'emprunter ou le rendre.

---

### Installation et Lancement 🛠️

Ce projet est conçu pour être lancé facilement avec Docker Compose, ce qui simplifie la configuration de l'environnement.

1. **Prérequis** : Assurez-vous d'avoir Docker et Docker Compose installés sur votre machine.
2. **Cloner le dépôt** :
```sh
git clone https://github.com/votre-nom-utilisateur/container-labs.git
cd container-labs/python-fastapi
```

3. Configuration des variables d'environnement :

-   Créez un fichier ```.env``` à la racine du projet.
-   Copiez-y les variables d'environnement nécessaires pour la connexion à la base de données et le port de l'application.
	
```sh
PORT_APP=8000
DB_USER=root
DB_PASS=password
DB_NAME=library_db
DB_HOST=db
DB_PORT=5432
```

4. **Lancement des conteneurs**:
- L'application sera lancée avec une base de données PostgreSQL.
- Utiliser la commande suivante pour construire les images et démarrer les conteneurs :
```sh
docker compose up -d --build
``` 
5. **Vérification de l'API**:
- Une fois les conteneurs démarrés, l'API est accessible à l'adresse suivante : ```http://localhost:8000```.
- Vous pouvez consulter la documentation interactive de FastAPI à cette adresse : ```http://localhost:8000/docs```.

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
### Prochaines Étapes ✨

- Développement du Front-End Flutter : Créer l'application mobile pour interagir avec l'API, en intégrant un scanner de code-barres pour le libre-service.

- Authentification et Autorisation : Mettre en place un système de rôles (administrateur vs. membre) pour sécuriser les routes.

- Gestion des Transactions : Ajouter un modèle de données pour enregistrer et suivre l'historique des prêts et des ventes.

- Amélioration de la gestion du stock : Mettre en place des fonctionnalités pour gérer les stocks de vente et de prêt séparément.

---
Si vous souhaitez en discuter ou si vous avez des questions, n'hésitez pas à me contacter par e-mail ou [LinkedIn](https://www.linkedin.com/in/el-beressa/). Je serais ravi d'échanger avec vous.
