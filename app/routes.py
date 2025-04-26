from flask import render_template, flash, redirect, url_for, request
from app import app, db # Importa la instancia de app y db
from app.models import Producto # Importa tus modelos para interactuar con la BD
from .forms import AddProductForm, ModifyProductForm, SearchProductForm, SearchProductFormByID


@app.route('/')
@app.route('/index')
def index():
    # Ejemplo básico: obtener algunos usuarios de la base de datos
    producto = Producto().query.all()
    return render_template('index.html', title='Inicio', producto=producto)

# Ejemplo de una ruta para añadir un producto (simplificado)
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()

    if form.validate_on_submit():
        nombre = form.nombre.data
        cantidad = form.cantidad.data
        precio = form.precio.data
        categoria = form.categoria.data

        producto = Producto(nombre=nombre, cantidad=cantidad, precio=precio, categoria=categoria)
        db.session.add(producto)
        db.session.commit()
        flash(f'Producto {nombre} añadido con éxito!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_product.html', title='Añadir Producto', form=form)

@app.route('/list_products')
def list_products():
    # Obtener todos los productos de la base de datos
    productos = Producto.query.all()
    return render_template('list_products.html', title='Lista de Productos', productos=productos)

@app.route('/search_product', methods=['GET', 'POST'])
def search_product():
    form = SearchProductForm()
    productos = []

    if form.validate_on_submit():
        nombre = form.nombre.data
        cantidad = form.cantidad.data
        precio = form.precio.data
        categoria = form.categoria.data

        # Construir la consulta basada en los campos proporcionados
        query = Producto.query

        if nombre:
            query = query.filter(Producto.nombre.ilike(f'%{nombre}%'))
        if cantidad:
            query = query.filter(Producto.cantidad == cantidad)
        if precio:
            query = query.filter(Producto.precio == precio)
        if categoria:
            query = query.filter(Producto.categoria.ilike(f'%{categoria}%'))

        productos = query.all()

        
        if not productos:
            flash('No se encontraron productos que coincidan con los criterios de búsqueda.')
        else:
            return render_template('list_products.html', title='Lista de Productos', productos=productos)   

    return render_template('search_product.html', title='Buscar Producto', form=form, productos=productos)


@app.route('/modify_product', methods=['GET', 'POST'])
def modify_product():
    search_product_by_id_form = SearchProductFormByID()

    if search_product_by_id_form.validate_on_submit():
        id = search_product_by_id_form.id.data
        producto = Producto.query.get(id)

        if producto:
            modify_product_form = ModifyProductForm(obj=producto)
            print(modify_product_form)
            return render_template('modify_product.html', title='Modificar Producto', form=modify_product_form, producto=producto)
        else:
            flash('Producto no encontrado.')

    return render_template('search_product_by_id.html', back_to='modify_product',
                           boton ='Modificar Producto',
                           class_boton = 'bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700 w-full',
                           title='Buscar Producto por ID', form=search_product_by_id_form)

@app.route('/modify_product2', methods=['GET', 'POST'])
def modify_product2():
    form = ModifyProductForm()

    if form.validate_on_submit():
        id = form.id.data
        producto = Producto.query.get(id)

        if producto:
            producto.nombre = form.nombre.data
            producto.cantidad = form.cantidad.data
            producto.precio = form.precio.data
            producto.categoria = form.categoria.data

            db.session.commit()
            print (f'Producto {producto.nombre} modificado con éxito!')
            flash(f'Producto {producto.nombre} modificado con éxito!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Producto no encontrado.')

    return render_template('modify_product.html', title='Modificar Producto', form=form)

@app.route('/delete_product', methods=['GET', 'POST'])
def delete_product():
    search_product_by_id_form = SearchProductFormByID()

    if search_product_by_id_form.validate_on_submit():
        id = search_product_by_id_form.id.data
        producto = Producto.query.get(id)

        if producto:
            db.session.delete(producto)
            db.session.commit()
            flash(f'Producto {producto.nombre} eliminado con éxito!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Producto no encontrado.', 'error')

    return render_template('search_product_by_id.html', 
                            boton = "Eliminar Producto",
                            class_boton = 'bg-red-500 text-white px-4 py-2 rounded hover:bg-red-700 w-full',
                            back_to='/delete_product', title='Buscar Producto por ID', form=search_product_by_id_form)

@app.route('/modify_product2', methods=['GET', 'POST'])
def delete_product2():
    form = ModifyProductForm()

    if form.validate_on_submit():
        id = form.id.data
        producto = Producto.query.get(id)

        if producto:
            producto.nombre = form.nombre.data
            producto.cantidad = form.cantidad.data
            producto.precio = form.precio.data
            producto.categoria = form.categoria.data

            db.session.commit()
            print (f'Producto {producto.nombre} modificado con éxito!')
            flash(f'Producto {producto.nombre} modificado con éxito!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Producto no encontrado.')

    return render_template('modify_product.html', title='Modificar Producto', form=form)