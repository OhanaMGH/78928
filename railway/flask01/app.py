from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "<h1>Hola</h1><p>Lorem ipsum</p>"

@app.route('/a')
def fun1():
    return "<h1>Lorem ipsum</h1><p>Ruta 1</p>"

@app.route('/xml')
def xml():
    return Response('<?xml version="1.0"?><nombre>John</nombre>',mimetype='application/xml')

@app.route('/json')
def algo():
    return Response('{"nombre":"John"}', mimetype='application/json')

if __name__ == "__main__":
    # Acepta conexión desde todas las ips
    app.run(host = "0.0.0.0", debug = True)