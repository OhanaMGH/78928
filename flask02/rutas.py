from flask import flask from Flask, render_template
from modelos import Producto
#crear instancia
app = Flask(__name__)


#definir una función
def inicio():
    #crear productos
    productos = [Producto("Manzanas", 12), Producto("Peras", 13)]
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)