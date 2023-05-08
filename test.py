import cv2

# Define the size of the images used to train the model
IMG_WIDTH = 100
IMG_HEIGHT = 100

# Load the trained model from the XML file
model = cv2.face.EigenFaceRecognizer_create()
model.read("facial_recognition_model.xml")

# Load a test image to recognize faces
testImage = cv2.imread("test_image.jpg", cv2.IMREAD_GRAYSCALE)
testImage = cv2.resize(testImage, (IMG_WIDTH, IMG_HEIGHT))

# Use the trained model to predict the label of the test image
label, distance = model.predict(testImage)

# Normalize the distance to a value between 0 and 1
maxDistance = model.getThreshold()
confidence = 1.0 - distance / maxDistance

# Print the predicted label and confidence level
print(f"Predicted label: {label}, confidence: {confidence}")
