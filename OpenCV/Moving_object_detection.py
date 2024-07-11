import cv2
import imageio
import numpy as np

gif = imageio.mimread('kakashi.gif')
gif_frames = [cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) for frame in gif]

# Initialize variables
first_frame = None
area = 500
key = 0 

while True:
    for frame in gif_frames:
        text = "Normal"
        frame = cv2.resize(frame, (500, 500))  # Resize frame
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        gaussian_img = cv2.GaussianBlur(gray_img, (21, 21), 0)  

        if first_frame is None:
            first_frame = gaussian_img
            continue

        img_diff = cv2.absdiff(first_frame, gaussian_img)  
        _, thresh_img = cv2.threshold(img_diff, 25, 255, cv2.THRESH_BINARY) 
        thresh_img = cv2.dilate(thresh_img, None, iterations=2) 

        contours, _ = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < area:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Moving object detected"

        cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) 
        cv2.imshow("gifFrame", frame) 

        key = cv2.waitKey(100) & 0xFF 
        if key == ord("q"):
            break

    if key == ord("q"):
        break

cv2.destroyAllWindows()
