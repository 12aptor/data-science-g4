from flask import Flask, request 

app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenido a la aplicación Flask!"

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre',' ')
    return f"<h1>Hola,{nombre}!</h1>"

@app.route('/sumar/<int:a>/<int:b>')
def sumar(a, b):
    resultado = a + b
    return f"<h1>La suma de {a} y {b} es {resultado}</h1>"

@app.route('/<operacion>/<int:num1>/<int:num2>')
def operaciones(operacion,num1, num2):
    """ dependiendo de la operación mostrar la suma,resta, multiplicación o división """
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        if num2 == 0:
            return "<h1>Error: División por cero no permitida</h1>"
        resultado = num1 / num2
    else:
        return "<h1>Error: Operación no válida</h1>"

    return f"<h1>El resultado de la {operacion} entre {num1} y {num2} es {resultado}</h1>"

app.run(debug=True)