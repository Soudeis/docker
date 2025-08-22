FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le code
COPY main.py .

# Installer les dépendances Python
RUN pip install --no-cache-dir fastapi uvicorn mysql-connector-python

# Exposer le port
EXPOSE 10000

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
