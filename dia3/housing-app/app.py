from flask import Flask,request,render_template
import joblib
import numpy as np
import sklearn

model = joblib.load('./model/housing-ml.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    result = 0
    if request.method == 'POST':
        rooms = int(request.form['rooms'])
        rooms_sc = sc_x.transform(np.array([[rooms]]))
        prediction = model.predict(rooms_sc)
        prediction_sc = sc_y.inverse_transform(prediction) * 1000
        result = round(prediction_sc[0][0],2)
        
    return render_template('index.html',result=result)

app.run(debug=True)