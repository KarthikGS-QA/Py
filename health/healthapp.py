from flask import Flask,render_template,request  # class,function,object
import numpy as np
import joblib

model=joblib.load("healthmodel.pkl")

app=Flask(__name__)

@app.route('/predict',methods=['GET','POST'])
def predict():

    test_data=[float(x) for x in request.form.values() ]
    print(f"Test Data is : {test_data}")

    pred=model.predict([test_data])

    result=pred[0]

    return render_template("homepagehealth.html",risk=result)  

@app.route('/login',methods=['GET','POST'])
def login():

    username=request.form['username']
    password=request.form['password']

    if username=="admin" and password=="admin123":
        return render_template("homepagehealth.html")
    else:
        return render_template("indexhealth.html",msg="Login Failed")
    

@app.route('/') # this is called default route
def index():
    return render_template("indexhealth.html")

 
app.run(debug=True, port=5000) # it will start server 
