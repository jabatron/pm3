# pm3
Practica Modulo 3


Enunciado de la Práctica
Título: Sistema de Gestión de Inventario con Base de Datos
Descripción: Crear una aplicación en Python que simule un sistema de gestión de
inventario utilizando una base de datos MySQL. La aplicación debe permitir a los
usuarios realizar las siguientes acciones:
1. Agregar un producto: Permite al usuario agregar un producto al inventario.
Los productos deben tener atributos como nombre, cantidad, precio y
categoría.
2. Mostrar todos los productos: Muestra una lista de todos los productos
disponibles en el inventario.
3. Buscar un producto: Permite al usuario buscar un producto por nombre.
4. Actualizar un producto: Permite al usuario actualizar la información de un
producto, como la cantidad o el precio.
5. Eliminar un producto: Permite al usuario eliminar un producto del
inventario.
Requisitos:
1. Utiliza una base de datos MySQL para almacenar la información del
inventario.
2. Implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para
gestionar los productos en la base de datos.
3. Utiliza la biblioteca mysql-connector-python o similar para conectar y
realizar operaciones en la base de datos.
4. Implementa un menú que permita al usuario seleccionar una acción
(agregar, mostrar, buscar, actualizar o eliminar un producto).
5. Implementa gestión de errores para manejar situaciones como:
• Intentar agregar un producto con un nombre que ya existe.
• Intentar buscar, actualizar o eliminar un producto que no existe.
• Manejo de errores de conexión a la base de datos.
Instrucciones:
1. Crea una base de datos MySQL y una tabla para almacenar la información
de los productos.
2. Crea una clase Producto con atributos para el nombre, cantidad, precio y
categoría.
3. Crea una clase GestionInventario que contenga métodos para agregar,
mostrar, buscar, actualizar y eliminar productos en la base de datos.
4. Implementa un menú que permita al usuario seleccionar una acción.
5. Utiliza consultas SQL para realizar las operaciones CRUD en la base de
datos.
6. Implementa manejo de excepciones para capturar y manejar errores
relacionados con la base de datos y las operaciones de inventario.
Entrega: Los estudiantes deben entregar el código fuente de la aplicación junto
con las instrucciones para configurar la base de datos MySQL y un script SQL para
crear la tabla de productos.


