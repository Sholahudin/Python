import cv2

# this is our image or video
# img_file = 'car.jpeg'
video = cv2.VideoCapture('video2.mp4')

# this is the pre-trained file that has learned to classify car
classifier_file = 'car_detector.xml'
classifier_file_2 = 'haarcascade_fullbody.xml'

# create classifier
car_tracker = cv2.CascadeClassifier(classifier_file)
pedestrian_tracker = cv2.CascadeClassifier(classifier_file_2)

while True:

    #read the current frame
    (read_succesful, frame) = video.read()

    # safe code
    if read_succesful:
        # convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # detect the cars
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrian = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)

    for (x, y, w, h) in pedestrian:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    # Display
    cv2.imshow('Clever Programmer', frame)

    # Not close the window until any key pressed
    cv2.waitKey(1)

# Release the videocapture object
video.release()

"""
    
# create open cv image
img = cv2.imread(img_file)

# create classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

# convert to grayscale
black_n_white = cv2.cvtColor(img, COLOR_BGR2GRAY)

cars = car_tracker.detectMultiScale(black_n_white)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

# Display
cv2.imshow('Clever Programmer', img)

# Not close the window until any key pressed
cv2.waitKey()

print('Code Completed')
"""