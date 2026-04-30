import cv2

cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



image=cv2.imread("multiFace.jpg")   #in imread(imageName,0)  0 is used if we need image in black and white

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face=cascade.detectMultiScale(gray,1.1,5)

print(face)

# print(type(face))

for x,y,w,h in face:

    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)


# print(image)

# print( type(image))

cv2.imshow("demo", image)

cv2.waitKey()  #wait till we click any button




