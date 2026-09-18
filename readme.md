# Intialiser l'environnement virtuel

```sh
python -m venv .venv
```

# Activer l'environnement virtuel

```sh
.venv\Scripts\activate
```

# Installer les dépendences

```sh
pip install sqlalchemy sqlalchemy-access pyodbc fastapi[standard]
pip freeze > requirements.txt
```