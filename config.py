import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-secreta-muy-dificil' # ¡Cambiar esto!
    # Configuración de la base de datos SQLite
    # SQLAlchemy necesita la ruta absoluta al archivo de la base de datos
    # Puedes usar 'sqlite:///:memory:' para una base de datos en memoria (no persistente)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Desactiva el seguimiento de modificaciones innecesario