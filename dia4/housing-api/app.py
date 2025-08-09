from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'title': 'FLASK API VERSION 1.0',
        'message': 'Bienvenido a mi API con Flask.'
    }
    
    return jsonify(context)

app.run(debug=True)
           