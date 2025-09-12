# Containerization & DevOps Recipes

Bienvenue dans ma collection de configurations pour des applications conteneurisées.

Ce dépôt regroupe des exemples de configurations et de déploiements pour diverses applications et services, en utilisant des technologies comme **Docker** et **Podman**. L'objectif est de fournir des "recettes" claires et prêtes à l'emploi pour le développement et le déploiement.

---
### 📦 Technologies et Outils

* **Moteurs de conteneurisation :** `Docker` | `Podman`
* **Orchestration :** `Docker Compose`
* **Serveurs web & Reverse Proxies :** `Nginx` | `Nginx Proxy Manager` | `Caddy`
* **Systèmes d'exploitation :** `Linux` `Debian` `Alpine` `LXC`
* **Plateforme de virtualisation :** `Proxmox`
* **Bases de données :** `PostgreSQL`, `MySQL`

---

### 📂 Structure du dépôt

Chaque dossier contient un projet spécifique, avec ses propres fichiers de configuration et une documentation détaillée dans son `README.md`.

---

### 🚀 Comment utiliser ces recettes

Chaque dossier est autonome. Il suffit de naviguer vers le répertoire du projet qui vous intéresse et de suivre les instructions du `README.md` correspondant. En général, les configurations peuvent être lancées avec une seule commande :

`docker-compose up -d`
ou, pour les environnements Podman :
`podman-compose up -d`

🌱 Contributions

Ces exemples sont le reflet de mes pratiques de travail. Si vous avez des suggestions ou des améliorations, n'hésitez pas à ouvrir une "issue" ou à soumettre une "pull request".
