import cv2
import os
import numpy as np
# Define the size of the images used to train the model
IMG_WIDTH = 100
IMG_HEIGHT = 100

# Read the list of training images and corresponding labels from a file
images = []
labels = []
with open('training_data.txt') as file:
    for line in file:
        imagePath, label = line.strip().split()
        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
        images.append(image)
        labels.append(int(label))

# Train the model using the training images and labels
model = cv2.face.EigenFaceRecognizer_create()
print(labels)
model.train(np.array(images), np.array(labels))

# Save the trained model to a file
model.save('ad.xml')
