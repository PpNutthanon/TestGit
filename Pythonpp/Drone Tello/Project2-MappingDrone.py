from djitellopy import tello
import Keypress as kp
from time import sleep
import numpy as np
import cv2
import math
import pygame

#Todo: Create Parameters
forward_speed = 117/10 # Forward speed in cm/s (15cm/s)
angular_speed = 360/10 # Angular speed in degrees/s (50 degree/s)
interval = 0.25

distance_interval = forward_speed * interval
angular_interval  = angular_speed * interval


x, y = 500, 500
a = 0
yaw = 0
kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

points = [(0,0), (0,0)]

def getKeyboardInput():
        lr, fb, ud, yv, = 0, 0, 0, 0
        speed = 15
        angular_interval = 50
        global x, y, yaw, a
        d = 0
        if kp.getkey("LEFT"): 
            lr = -speed
            d = distance_interval
            a = -180
        elif kp.getkey("RIGHT"): 
            lr = speed
            d = -distance_interval
            a = 180

        if kp.getkey("UP"): 
            fb = speed
            d = distance_interval
            a = 270
        elif kp.getkey("DOWN"): 
            fb = -speed
            d = -distance_interval
            a = -90

        if kp.getkey("w"): ud = speed
        elif kp.getkey("s"): ud = -speed

        if kp.getkey("a"): 
            yv = -angular_speed
            yaw -= angular_interval

        elif kp.getkey("d"): 
            yv = angular_speed
            yaw += angular_interval

        if kp.getkey("q"): yv = drone.land(); sleep(3)
        if kp.getkey("e"): yv = drone.takeoff()

        sleep(interval)
        a += yaw
        x += int(d*math.cos(math.radians(a)))
        y += int(d*math.sin(math.radians(a)))


        return [lr, fb, ud, yv]

def drawpoints(img, points):
        for point in points:
            cv2.circle(img, point, 5, (0,0,255), cv2.FILLED)
        cv2.circle(img, point, 8, (0,255,0), cv2.FILLED)    
        cv2.putText(img,f"({(points[-1][0]-500)/100},{(points[-1][1]-500)/100})m",points[-1][0]+10, points[-1][1]+30, cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)


while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0],vals[1],vals[2],vals[3])
        
    img = np.zeros((1000,1000,3), np.uint8) #Todo: unint8 = 2^8 so the range of value between 0-255
    if (points[-1][0]) != vals[4] or points[-1][1] != vals[5]: 
        points.append((vals[4], vals[5]))
    drawpoints(img, points)
    cv2.imshow("Output",img)
    cv2.waitKey(1)