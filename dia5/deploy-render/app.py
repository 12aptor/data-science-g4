from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from decouple import config
from flask_cors import CORS

import joblib
import numpy as np
import sklearn

model = joblib.load('./model/housing-ml.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

app = Flask(__name__)
CORS(app)

#### CONFIGURACION DE SQLALCHEMY ####
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## CREAMOS LA TABLA HOUSING
db = SQLAlchemy(app)
class Housing(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rooms = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Double,nullable=True)
    
    def __init__(self,rooms):
        self.rooms = rooms
        
### CREAMOS UN ESQUEMA PAARA SERIALIZAR LOS DATOS
ma = Marshmallow(app)
class HousingSchema(ma.Schema):
    id = ma.Integer()
    rooms = ma.Integer()
    price = ma.Float()

## REGISTRAMOS LA TABLA EN LA BASE DE DATOS
db.create_all()
print('Base de datos creada')

def predict_price(rooms):
    rooms_sc = sc_x.transform(np.array([[rooms]]))
    prediction = model.predict(rooms_sc)
    prediction_sc = sc_y.inverse_transform(prediction) * 1000
    price = round(float(prediction_sc[0][0]), 2)
    return price

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
    price = predict_price(rooms)
    print(price)
    new_housing = Housing(rooms)
    new_housing.price = price
    #insertamos el nuevo registro en la base de datos
    db.session.add(new_housing) # insert into housing values(null,rooms)
    
    db.session.commit()
    
    data_schema = HousingSchema()
    
    context = {
        'status':True,
        'message': 'Registro insertado correctamente',
        'content': data_schema.dump(new_housing)
    }
    
    return jsonify(context),201

@app.route('/housing',methods=['GET'])
def get_data():
    data = Housing.query.all() # select * from housing
    
    data_schema = HousingSchema(many=True)
    
    context = {
        'status':True,
        'message': 'listado de registros',
        'content': data_schema.dump(data)
    }
    
    return jsonify(context),200

@app.route('/housing/<int:id>',methods=['GET'])
def get_data_by_id(id):
    data = Housing.query.get(id) # select * from housing where id = id
    data_schema = HousingSchema()
    
    context = {
        'status': True,
        'message': 'Registro encontrado',
        'content': data_schema.dump(data) if data else None
    }
    
    return jsonify(context), 200 if data else 404

@app.route('/housing/<int:id>',methods=['PUT'])
def update_data(id):
    data = Housing.query.get(id)
    if not data:
        return jsonify({'status': False, 'message': 'Registro no encontrado'}), 404
    
    rooms = request.json['rooms']
    price = predict_price(rooms)
    
    data.rooms = rooms
    data.price = price
    db.session.commit()
    
    data_schema = HousingSchema()
    context = {
        'status': True,
        'message': 'Registro actualizado correctamente',
        'content': data_schema.dump(data)
    
    }
    return jsonify(context), 200

@app.route('/housing/<int:id>',methods=['DELETE'])
def delete_data(id):
    data = Housing.query.get(id)
    
    if not data:
        return jsonify({'status': False, 'message': 'Registro no encontrado'}), 404
    
    db.session.delete(data) #delete from housing where id = id
    db.session.commit()
    
    context = {
        'status': True,
        'message': 'Registro eliminado correctamente'
    }
    
    return jsonify(context), 200

if __name__ == '__main__':
    app.run()
           