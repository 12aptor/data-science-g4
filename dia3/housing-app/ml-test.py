import joblib
import numpy as np
import sklearn

model = joblib.load('./model/housing-ml.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

print(" Scikit-learn version:", sklearn.__version__)
print(f" sc_x mean: {sc_x.mean_}, scale: {sc_x.scale_}")
print(f" sc_y mean: {sc_y.mean_}, scale: {sc_y.scale_}")