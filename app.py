from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('classifier.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    Humidity = (request.form.get('Humidity'))
    Temperature = (request.form.get('Temperature'))
    Soil = (request.form.get('Soil'))
    Rainfall = (request.form.get('Rainfall'))

    # prediction
    result = model.predict(np.array([[Humidity,Temperature,Soil,Rainfall]]))
    if result[0] == 0:
        result = 'SUNNY DAY'
    else:
        result = 'RAINY DAY'




    return render_template('index.html',result=str(result))


if __name__ == '__main__':
    app.run(debug=True)