# Utiliser une image officielle de Python
FROM python:3.11

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r ./app/requirements.txt

# Exposer le port 8000
EXPOSE 8000

# Démarrer Django
CMD ["python", "app/manage.py","runserver", "0.0.0.0:8000"]
