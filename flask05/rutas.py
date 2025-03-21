from flask import Flask, render_template, request, Response, redirect, url_for
import sqlite3

app = Flask(__name__)

#row_factoy es un diccionario
#productos = [Producto("Impresora", 500), Producto("Computadora", 620), Producto("Mouse", 150)]


@app.route('/')
def index():
    con = conexion()
    productos = con.execute('SELECT * FROM productos').fetchall()
    con.close()
    return render_template('productos.html', productos=productos)


@app.route('/editar/<id>')
def editar(id):
    con = conexion()
    p = con.execute('select * from productos where id = ?', (id)).fetchone()
    con.close()
    #se crea la plantilla para editar el producto deseado
    return render_template('editar.html', producto = p)

@app.route('/guardar', methods=['POST'])
def guardar():
    n = request.form.get('nombre')
    p = request.form.get('precio')
    id = request.form.get('id')
    print(f"{n} {p} {id}")
    con = conexion()
    con.execute("UPDATE productos SET nombre = ?, precio = ? WHERE id = ?", (n, p, id))
    con.commit()
    con.close()
    return Response("Guardado", headers={'Location': '/'}, status=302)


@app.route('/eliminar/<id>')
def eliminar(id):
    con = conexion()
    con.execute('DELETE FROM productos WHERE id = ?', (id,))
    con.commit()
    con.close()
    return Response("Eliminado", headers={'Location': '/'}, status=302)


@app.route('/crear', methods=['POST'])
def crear():
    n = request.form.get('nombre')
    p = request.form.get('precio')
    con = conexion()
    con.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', (n, p))
    con.commit()
    con.close()
    return redirect(url_for('index'))  


def conexion():
    con = sqlite3.connect('base de datos.db')
    con.row_factory = sqlite3.Row
    return con


def iniciar_db():
    con = conexion()
    # Se crea la tabla en caso de que no exista
    con.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    con.commit()
    con.close()


if __name__ == '__main__':
    iniciar_db()  # Llamar a esta función para asegurarse de que la base de datos y la tabla se crean
    app.run(host='0.0.0.0', debug=True)
