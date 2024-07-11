import cv2
import imageio
import imutils

gif = imageio.mimread('kakashi.gif')
gif_frames = [cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) for frame in gif]
firstFrame = None
area = 500

while True:
    for frame in gif_frames:
        text = "Normal"
        frame = imutils.resize(frame, width=500)
        grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

        if firstFrame is None:
            firstFrame = gaussianImg
            continue

        imgDiff = cv2.absdiff(firstFrame, gaussianImg)
        threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
        threshImg = cv2.dilate(threshImg, None, iterations=2)
        cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cnts = imutils.grab_contours(cnts)
        for c in cnts:
            if cv2.contourArea(c) < area:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Moving object detected"

        print(text)
        cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow("gifFrame", frame)

        key = cv2.waitKey(100) & 0xFF
        if key == ord("q"):
            break

    if key == ord("q"):
        break

cv2.waitKey(100000)
