import cv2

camera = cv2.VideoCapture(0)
#camera is object of the class VideoCapture

flag,frame=camera.read()

if flag:
    cv2.imshow("result",frame)
    cv2.waitKey()

camera.release()
