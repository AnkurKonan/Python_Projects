import cv2
import os
import numpy as np

dataset_path = '/Users/ankur/PycharmProjects/pythonProject/Face_Recognition/Faces_of_Family'
model_path = 'Face_Training.yml'

recognizer = cv2.face.LBPHFaceRecognizer_create()

face_samples = []
labels = []
label_dict = {}

def get_images_and_labels(dataset_path):
    label_id = 0

    for person_name in os.listdir(dataset_path):
        person_path = os.path.join(dataset_path, person_name)

        if not os.path.isdir(person_path):
            continue

        label_dict[label_id] = person_name

        for image_name in os.listdir(person_path):
            image_path = os.path.join(person_path, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if image is None:
                continue

            face_samples.append(image)
            labels.append(label_id)
        label_id += 1

    return face_samples, labels

faces, ids = get_images_and_labels(dataset_path)
recognizer.train(faces, np.array(ids))
recognizer.save(model_path)

print(f'Training completed. Model saved as {model_path}.')
