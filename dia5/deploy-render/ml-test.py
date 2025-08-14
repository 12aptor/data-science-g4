import joblib
import numpy as np
import sklearn

model = joblib.load('./model/housing-ml.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

print(" Scikit-learn version:", sklearn.__version__)
print(f" sc_x mean: {sc_x.mean_}, scale: {sc_x.scale_}")
print(f" sc_y mean: {sc_y.mean_}, scale: {sc_y.scale_}")

rooms = int(input("Ingrese el número de habitaciones: "))
rooms_sc = sc_x.transform(np.array([[rooms]]))
#print(f"rooms_sc: {rooms_sc}")

prediction = model.predict(rooms_sc)
#print(f"Predicción: {prediction}")

prediction_sc = sc_y.inverse_transform(prediction) * 1000
print(f' El precio de un departamento con {rooms} habitaciones es: $ {prediction_sc[0][0]:.2f}')