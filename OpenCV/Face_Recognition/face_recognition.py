import cv2
import os
import numpy as np

model_training = 'Face_Training.yml'
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(model_training)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

label_dict = {
    0: 'Ankur',
    1: 'Father',
    2: 'Mother'
}

image_path = '/Users/ankur/PycharmProjects/pythonProject/Ankur.jpeg'
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not load image.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    label_id, confidence = recognizer.predict(roi_gray)

    if confidence < 100:
        label = label_dict[label_id]
        confidence_text = f'{round(100 - confidence, 2)}%'
    else:
        label = 'Unknown'
        confidence_text = ''

    cv2.rectangle(image, (x, y), (x+w, y+h), (102, 216, 68), 2)
    cv2.putText(image, f'{label} {confidence_text}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (102, 216, 68), 2)

cv2.imshow('Face Recognition', image)

cv2.waitKey(20000)
cv2.destroyAllWindows()
