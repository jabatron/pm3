from app import db # Importa la instancia de db creada en __init__.py


""" 
    Permite al usuario agregar un producto al inventario.
    Los productos deben tener atributos como nombre, cantidad, precio y
    categoría.
 """
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(64), index=True, unique=True)
    cantidad = db.Column(db.Integer, index=True)
    precio = db.Column(db.Float, index=True)
    categoria = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<Producto {self.name}>'