import cv2
import random

cam=cv2.VideoCapture(0)

cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    flag,frame = cam.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face=cascade.detectMultiScale(gray,1.1,5)

    print(face)

    # print(type(face))

    for x,y,w,h in face:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)



    cv2.imshow("demo", frame)
    k=cv2.waitKey(1)

    if k==ord('q'):
        break

    if k==ord('s'):
        x,y,w,h=face[0]    #let us fetch the first face after clicking s
        
        roi=frame[y:y+h,x:x+w]   #Croping of the face

        roi=cv2.resize(roi,(300,300))
        
        random_num=random.randint(1,100)
        fileName=f"./Dataset/4/person{random_num}.jpg"

        cv2.imwrite(fileName,roi)

cam.release()