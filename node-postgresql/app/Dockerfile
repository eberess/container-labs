# Utiliser une image de base Node.js
FROM node:18-alpine

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier le fichier package.json pour installer les dépendances
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste du code de l'application
COPY . .

# Exposer le port de l'application
EXPOSE 3001

# Commande pour démarrer l'application
CMD ["npm", "start"]
