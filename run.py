from app import app, db
from app.models import Producto # Importa tus modelos si quieres acceder a ellos en la shell


@app.shell_context_processor
def make_shell_context():
    """Permite acceder a 'app' y 'db' y modelos en el shell de Flask"""
    return {'app': app, 'db': db, 'Producto': Producto} # Añade aquí tus otros modelos si los tienes

if __name__ == '__main__':
    # Crear las tablas de la base de datos si no existen
    # Esto es simple para un ejemplo, en producción podrías usar migraciones (como Flask-Migrate)
    with app.app_context():
         db.create_all()
    app.run(debug=True) # debug=True para desarrollo, False para producción