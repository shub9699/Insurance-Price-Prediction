from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index1.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Age = int(request.form['Age'])
        BMI=float(request.form['BMI'])
        Children=int(request.form['Children'])
        region=request.form['region']
        if(region=='southwest '):
                region_southwest=1
                region_southeast=0
                region_northwest=0
        elif(region=='southeast'):
                region_southwest=0
                region_southeast=1
                region_northwest=0
        elif(region=='northwest'):
                region_southwest=0
                region_southeast=0
                region_northwest=1
        else:
             region_southwest=0
             region_southeast=0
             region_northwest=0
        Gender=request.form['Gender']
        if(Gender=='Female'):
            Gender=1
        else:
            Gender=0	
        Smoker=request.form['smoke']
        if(Smoker=='smoker'):
            Smoker=1
        else:
            Smoker=0
        prediction=model.predict([[Age,BMI,Children,region,Gender,smoke]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index1.html',prediction_texts="Sorry you cannot get the insurance")
        else:
            return render_template('index1.html',prediction_text="You can get insurance of {}".format(output))
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

