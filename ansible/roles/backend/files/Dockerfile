# Utiliser l'image Python officielle version 3.8
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier server.py dans le conteneur
COPY backend/server.py .

# Installer le connecteur MySQL pour Python
RUN pip install mysql-connector-python

# Commande à exécuter lorsque le conteneur démarre
CMD ["python", "server.py"]
