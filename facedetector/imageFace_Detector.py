import cv2
from random import randrange

#Load some pre-trained data on face frontals from opencv
trained_faced_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
img = cv2.imread('hpmany.jpeg')

#make grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_faced_data.detectMultiScale(grayscaled_img)

for (x, y, w, h) in face_coordinates: 
    cv2.rectangle(img, (x,y), (x+w, y+h),(0, 255, 0), 2)


#print(face_coordinates)

cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()



print('Code Completed')