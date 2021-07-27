import cv2

# Our video
video = cv2.VideoCapture('Pedestrians Compilation.mp4')

# Our pre-trained car and pedestrian classifiers
car_tracker_file = 'car_detector.xml'
pedestrian_tracker_file = 'pedestrian_detector.xml'

# Create Car Classifiers
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

# Run forever until car stops or something. or crashes.
while True:
    # Read the current frame
    (read_successful, frame) = video.read()

    # Safe Coding.
    if read_successful:
        # Must convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect cars And pedestrians
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    print(cars) # [top-left point X, top-left pointY, width, height]

    # Draw rectangles around the cars
    # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Draw rectangles around the pedestrians
    # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Display the image with the faces spotted
    cv2.imshow('Matamong Car And Pedestrian Detector', frame)

    # Don't autoclose (Wait here in the code and listen for a key press)
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key==81 or key == 113:
        break

# Release the VideoCapture object
video.release()

print("Code Complete")