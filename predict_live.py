import cv2

from myapi import saveEmp

cam=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recog=cv2.face.LBPHFaceRecognizer_create()

recog.read("facemodel.yml")  # Load your model

names={0:"Karthik G S",1:"Sunil",2:"KB",3:"Tirthu",4:"Kiran"}

while True:
    
    flag,frame=cam.read()
    
    
    
    if flag:
        
        
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        faces=cascade.detectMultiScale(gray,1.1,5)
        
        if len(faces) > 0 :
            
            x,y,w,h=faces[0]  # fetch 1st person
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
            
            roi=gray[y:y+h,x:x+w]  # crop the face
            
            roi=cv2.resize(roi,(300,300))
            
            id,confi=recog.predict(roi)
            
            detected_name="Un-known"
            
            
            
            if confi < 30:
                detected_name=names[id]
                saveEmp(detected_name)
                
            cv2.putText(frame, detected_name, (50, 50),cv2.FONT_HERSHEY_COMPLEX,1.2, (255, 0, 0), 3)
            
            print(f"Id : {id} , Confidence : {confi}")
            
                
        
        cv2.imshow("Face Recrognition",frame)
              
        k=cv2.waitKey(1)
        if k==ord('q'):
            break


cam.release()
