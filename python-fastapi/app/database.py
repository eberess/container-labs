from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Récupérer les variables d'environnement
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# URL de connexion à la base de données
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Créer un moteur de base de données
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Créer une session de base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

<<<<<<< HEAD
# Déclarer la base pour les modèles
=======
# Déclare la base pour les modèles
>>>>>>> 33d59440a3122874a3707a7e08e51eab07d5cd4d
Base = declarative_base()

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
<<<<<<< HEAD
        db.close()
=======
        db.close()
>>>>>>> 33d59440a3122874a3707a7e08e51eab07d5cd4d
