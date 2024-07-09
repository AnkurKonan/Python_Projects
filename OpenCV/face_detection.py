import cv2 

img = cv2.imread('/Users/ankur/PycharmProjects/pythonProject/group_of_people.png')
cv2.imshow('Group of 5 people', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
c = cv2.CascadeClassifier('haar_face.xml')
faces = c.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces)}')

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv2.imshow('Detected Faces', img)

cv2.waitKey(0)
