import cv2
import numpy as np
from djitellopy import tello
import time

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()
me.takeoff()

me.send_rc_control(0, 0, 25, 0)
time.sleep(2.2)

w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.1, 0.0, 0.0]  # modify the PID values
pError = [0,0]

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

def trackFace(info, w, h, pid, pError):
    x, y = info[0]
    area = info[1]
    fb = 0
    error_x = x - w // 2
    error_y = y - h // 2  # calculate the vertical error
    speed_x = pid[0] * error_x + pid[1] * (error_x - pError[0])
    speed_y = pid[0] * error_y + pid[1] * (error_y - pError[1])  # calculate the vertical speed
    speed_x = int(np.clip(speed_x, -100, 100))
    speed_y = int(np.clip(speed_y, -50, 50))  # limit the vertical speed

    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    elif area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0:
        fb = 20

    if x == 0:
        speed_x = 0
        error_x = 0
    if y == 0:  # if there's no face in the frame, don't adjust the vertical speed
        speed_y = 0
        error_y = 0

    print(f"speed_x: {speed_x}, speed_y: {speed_y}, error_x: {error_x}, error_y: {error_y}")  # debug print
    me.send_rc_control(0, fb, speed_y, speed_x)  # use the vertical speed to control the drone's up/down movement

    return [error_x, error_y]

cap = cv2.VideoCapture(0)
while True:

    _, img = cap.read()

    img = me.get_frame_read().frame

    img = cv2.resize(img, (w, h))

    img, info = findFace(img)

    pError = trackFace( info, w, h, pid, pError)

    print("Center", info[0], "Area", info[1])

    cv2.imshow("Output", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        me.land()

        break
