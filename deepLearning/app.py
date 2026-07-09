from flask import Flask,render_template,request
import os 
import cv2
import numpy as np
import joblib
import json

# app=Flask(__name__)

UPLOAD_FOLDER="deepLearning/static/uploads"

app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

model=joblib.load("deepLearning/rf_tomato_model.pkl")

IMG_size=64

def preprocess_image(image_path):
    img=cv2.imread(image_path)
    img=cv2.resize(img,(IMG_size,IMG_size))
    return img.reshape(1,-1)


@app.route('/')
def index():
    return render_template('deepLearning/templates/index.html')

@app.route('/predict',methods=['post'])
def predict():
    file=request.files['image']

    if file.filename=="":
        return "No file Selected"
    
    filepath=os.path.join(app.config['UPLOAD_FOLDER'],file.filename)

    file.save(filepath)

    features=preprocess_image(filepath)

    prediction=model.predict(features)

    class_name=['Bacterial Spot','Early Blight','Healty']

    result=class_name[prediction[0]]

    return render_template(
        "deepLearning/templates/result.html",
        image_path=filepath,
        result=result
    )

# app.run(debug=True,host="0.0.0.0")
