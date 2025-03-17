#!/bin/bash

# Supprimer les fichiers .pyc et .py
find . -path "*/migrations/*" -name "*.py" -not -path "*__init__*" -delete
find . -path "*/migrations/*.pyc" -delete  

# Supprimer la base de données
rm -f db.sqlite3

# Exécuter les migrations
python manage.py makemigrations
python manage.py migrate

# Créer un super utilisateur
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', '', 'password')" | python manage.py shell

# Générer des données fictives
python manage.py generate_dummy_data
