from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    nombre = request.args.get('nombre',' ')
    return render_template('index.html',nombre=nombre)

app.run(debug=True)