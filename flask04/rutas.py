from flask import Flask, render_template
from modelos import Producto
from flask import request
from flask import Response

app = Flask(__name__)

productos = [Producto("Impresora", 500), Producto("Computadora", 620), Producto("Mouse", 150)]
    

@app.route('/')

def inicio():
    #productos = [Producto("Impresora", 500), Producto("Computadora", 620), Producto("Mouse", 150)]
    return render_template('productos.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto,precio):
    #recuperar producto
    print(producto,precio)
    return render_template('editar.html', producto= producto, precio = precio)

@app.route('/guardar', methods=['POST'])
def guardar():
    n= request.form.get('nombre')
    p= request.form.get('precio')
    print(n,p)
    i = 0
    for e in productos:
        if e.nombre == n:
            productos[i] = Producto(n,p)
            print(f"{e.nombre} {e.precio}")
        i+=1
    return Response("guardado", headers={'Location': '/'}, status=302)

@app.route('/eliminar/<nombre>')
def eliminar(nombre):
    i = 0
    for e in productos:
        if e.nombre == nombre:
            productos.pop(i)
            print(f"{e.nombre} {e.precio}")
        i+=1
    return Response("Eliminado", headers={'Location': '/'}, status=302)

@app.route('/crear', methods=['POST'])
def crear():
    n = request.form.get('nombre')
    p = request.form.get('precio')

    # Verificar si el producto ya existe
    for e in productos:
        if e.nombre == n:
            return Response("Error: Producto ya existente", status=400)

    # Agregar el nuevo producto a la lista
    productos.append(Producto(n, p))
    print(f"Producto creado: {n} {p}")

    return Response("Producto creado", headers={'Location': '/'}, status=302)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)