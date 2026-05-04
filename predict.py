import cv2
from os import listdir
import numpy as np

recog=cv2.face.LBPHFaceRecognizer_create() 

recog.read("faceModel.yml")      # Load your model

testImage=cv2.imread("croppedFace.jpg",0)

id,confi = recog.predict(testImage)


print(f"ID = {id}, confidence = {confi} ")
cv2.imshow("testImage",testImage)
cv2.waitKey()
