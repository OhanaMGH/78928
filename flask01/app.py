from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola mundo"

@app.route('/despedir')
def despedir():
    return "adios!"

@app.route('/hola')
def hola():
    return '<h1 style="color:red;"">Hola!<h1>'

@app.route('/json')
def algo():
    return '{"nombre":"John"}'

@app.route('/xml')
def xml():
    return '<?xml version="1,0"?><nombre>John</nombre>'

if __name__ == "__main__":
    app.run(host='0.0.0.0',
    debug=True)