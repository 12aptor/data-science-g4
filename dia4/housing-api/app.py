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

@app.route('/housing',methods=['POST'])
def set_data():
    rooms = request.json['rooms']
    new_housing = Housing(rooms)
    #insertamos el nuevo registro en la base de datos
    db.session.add(new_housing) # insert into housing values(null,rooms)
    db.session.commit()
    
    context = {
        'status':True,
        'message': 'Registro insertado correctamente'
    }
    
    return jsonify(context),201

app.run(debug=True)
           