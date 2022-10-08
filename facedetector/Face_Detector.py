import cv2
from random import randrange

#Load some pre-trained data on face frontals from opencv
trained_faced_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
#img = cv2.imread('hpmany.jpeg')

#To Capture Video from webcame
webcam = cv2.VideoCapture(0) #zero artinya default webcam. kalau diganti direktori file juga bisa

while True:

    ### Read the current frame
    succesful_frame_read, frame = webcam.read()

    #make grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates = trained_faced_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates: 
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 255, 0), 2)

    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    #stop button
    if key==81 or key==113:
        break

webcam.release() #release webcamnya
print('Code Completed')