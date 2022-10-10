import cv2
from numpy import empty

# include the classifier
face_classifier = cv2.CascadeClassifier('../facedetector/haarcascade_frontalface_default.xml')
smile_classifier = cv2.CascadeClassifier('haarcascade_smile.xml')

# initialize the webcam / code 0 = webcam
webcam = cv2.VideoCapture(0)

while True:
    # read the webcam
    sucessfull_frame_read, frame = webcam.read()

    # convert the color to grayscale
    grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect them
    face_coordinates = face_classifier.detectMultiScale(grayscaled)
    #smile_coordinates = smile_classifier.detectMultiScale(grayscaled, scaleFactor = 1.7, minNeighbors = 20)

    # create rectangle when it is detected
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

        # Get the sub frame (using numpy N-dimensional array slicing)
        the_face = frame[y:y+h: , x:x+w]
        
        # the code below is to make sure the smile detect the area of face only
        grayscaled_face = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        smile_coordinates = smile_classifier.detectMultiScale(grayscaled_face, scaleFactor = 1.5, minNeighbors = 20)
        
        # Label this face as smiling
        if len(smile_coordinates) > 0:
            cv2.putText(frame,"smiling",(x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,255,255))

        # for (x_, y_, w_, h_) in smile_coordinates:
        #     cv2.rectangle(the_face, (x_,y_), (x_+w_, y_+h_), (0, 0, 255), 2)


    # show the read result of webcam
    cv2.imshow("Sholahudin's Webcam", frame)

    # wait key means it will wait any time before continue to next line
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

webcam.release()
cv2.destroyAllWindows()

print('Completed Code')