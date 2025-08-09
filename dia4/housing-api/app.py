from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#### CONFIGURACION DE SQLALCHEMY ####
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/db_mlg4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## CREAMOS LA TABLA HOUSING
db = SQLAlchemy(app)
class Housing(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rooms = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Double,nullable=True)
    
    def __init__(self,rooms):
        self.rooms = rooms

## REGISTRAMOS LA TABLA EN LA BASE DE DATOS
db.create_all()
print('Base de datos creada')

@app.route('/')
def index():
    context = {
        'title': 'FLASK API VERSION 1.0',
        'message': 'Bienvenido a mi API con Flask.'
    }
    
    return jsonify(context)

app.run(debug=True)
           