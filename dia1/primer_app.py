from flask import Flask, request 

app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenido a la aplicación Flask!"

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre',' ')
    return f"<h1>Hola,{nombre}!</h1>"

app.run(debug=True)