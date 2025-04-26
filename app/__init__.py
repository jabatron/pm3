from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config # Importa la clase de configuración

app = Flask(__name__) # Crea la instancia de la aplicación
app.config.from_object(Config) # Carga la configuración desde config.py

db = SQLAlchemy(app) # Inicializa Flask-SQLAlchemy

# Importa tus rutas y modelos. Importarlos aquí (generalmente al final)
# ayuda a evitar problemas de importación circular donde rutas o modelos
# necesitan acceder a 'app' o 'db' que están siendo creados en este archivo.
from app import routes, models # noqa: F401
