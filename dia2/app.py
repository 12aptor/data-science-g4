from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    resultado = 0
    if request.method == 'POST':
        origen = request.form['origen']
        resultado = int(origen) / 3.58
    return render_template('index.html',destino=resultado)

app.run(debug=True)