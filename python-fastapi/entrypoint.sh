#!/bin/sh

# Exécute un script Python pour s'assurer que la base de données est prête
python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"

# Lance l'application FastAPI
<<<<<<< HEAD
exec uvicorn main:app --host 0.0.0.0 --port 8000
=======
exec uvicorn main:app --host 0.0.0.0 --port 8000
>>>>>>> 33d59440a3122874a3707a7e08e51eab07d5cd4d
