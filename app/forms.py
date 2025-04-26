from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class AddProductForm(FlaskForm):
    """Formulario para añadir un producto."""
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    cantidad = IntegerField('Cantidad', validators=[DataRequired(), NumberRange(min=1)])
    precio = DecimalField('Precio', validators=[DataRequired(), NumberRange(min=0)], places=2)
    categoria = SelectField('Categoría', choices=[('Electrónica', 'Electrónica'), ('Ropa', 'Ropa'), ('Alimentos', 'Alimentos')], validators=[DataRequired()])
    submit = SubmitField('Añadir Producto')

class ModifyProductForm(FlaskForm):
    """Formulario para modificar un producto."""

    # id -> oculto, se puede usar para buscar el producto a modificar
    id = IntegerField('ID', validators=[DataRequired(), NumberRange(min=1)], render_kw={"readonly": True})
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    cantidad = IntegerField('Cantidad', validators=[DataRequired(), NumberRange(min=1)])
    precio = DecimalField('Precio', validators=[DataRequired(), NumberRange(min=0)], places=2)
    categoria = SelectField('Categoría', choices=[('Electrónica', 'Electrónica'), 
                                                  ('Ropa', 'Ropa'), 
                                                  ('Alimentos', 'Alimentos')], validators=[Optional()])
    submit = SubmitField('Modificar Producto')

class SearchProductForm(FlaskForm):
    """Formulario para buscar un producto."""
    nombre = StringField('Nombre', validators=[Optional(), Length(max=100)])
    cantidad = IntegerField('Cantidad', validators=[Optional(), NumberRange(min=1)])
    precio = DecimalField('Precio', validators=[Optional(), NumberRange(min=0)], places=2)
    categoria = SelectField('Categoría', choices=[('', 'Selecciona una Categoría'), 
                                                  ('Electrónica', 'Electrónica'), 
                                                  ('Ropa', 'Ropa'), 
                                                  ('Alimentos', 'Alimentos')], validators=[Optional()])
    submit = SubmitField('Buscar Producto')

class SearchProductFormByID(FlaskForm):
    """Formulario para buscar un producto por ID."""
    id = IntegerField('ID', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Buscar Producto')