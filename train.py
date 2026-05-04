import cv2
from os import listdir
import numpy as np

recog=cv2.face.LBPHFaceRecognizer_create()         #Linear Binary Pattren Histrogram (LBPH) 

rootDir="./dataset"

features=[]
lables=[]

i=0

for subFolder in listdir(rootDir):
    # print(subFolder)
    folders=f"{rootDir}/{subFolder}"
    
    for file in listdir(folders):
        filePath=F"{folders}/{file}"

        print(filePath)

        image=cv2.imread(filePath,0)
       
        # cv2.imshow("demo",image)
        # cv2.waitKey()

        features.append(image)
        lables.append(i)
    
    i=i+1

recog.train( features,np.array(lables))

recog.save("faceModel.yml")