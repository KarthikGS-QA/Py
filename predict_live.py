import cv2

cam=cv2.VideoCapture(0)

cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recog=cv2.face.LBPHFaceRecognizer_create() 

recog.read("faceModel.yml")      # Load your model

