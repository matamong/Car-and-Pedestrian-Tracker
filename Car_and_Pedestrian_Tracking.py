import cv2

# Our image
img_file = 'Car_image.png'

# Our pre-trained car classifier
classifier_file = 'car_detector.xml'

# Create OpenCV image (Read Fixel Data)
img = cv2.imread(img_file)


# Convert to grayscale (needed for haar cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create Car Classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

# Detect cars
cars = car_tracker.detectMultiScale(black_n_white)
print(cars) # [top-left point X, top-left pointY, width, height]

# Draw rectangles around the cars
# cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Display the image with the faces spotted
cv2.imshow('Matamong Car Detector', img)

# Don't autoclose (Wait here in the code and listen for a key press)
cv2.waitKey()



print("Code Complete")