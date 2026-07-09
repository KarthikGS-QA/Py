from flask import Flask,render_template,request
import numpy as np
import joblib

model=joblib.load("CropModel.pkl")

app=Flask(__name__)

@app.route('/login',methods=['get','post'])
def login():
    
    username=request.form['username']
    password=request.form['password']

    if username=="admin" and password=="admin123":
        return render_template("homepage.html")
    else:
        return render_template("index.html",msg=" Login Failed ")

@app.route('/predict',methods=['get','post'])
def predict():
    
    test_data=[float(x) for x in request.form.values()]

    print(f"Test data is : {test_data}")

    pred=model.predict([test_data])

    result=pred[0]

    print(f"result is : {result}")

    return render_template("homepage.html",crop=result)


@app.route('/') # this is called default route
def index():
    return render_template("index.html")



app.run(debug=True,port=8000)  # it will start server 
