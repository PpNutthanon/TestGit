from djitellopy import tello
import Keypress as kp
import time
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
global img


drone.streamon()

def getKeyboardInput():
        lr, fb, ud, yv, = 0, 0, 0, 0
        speed = 50
        if kp.getkey("LEFT"): lr = -speed
        elif kp.getkey("RIGHT"): lr = speed

        if kp.getkey("UP"): fb = speed
        elif kp.getkey("DOWN"): fb = -speed

        if kp.getkey("w"): ud = speed
        elif kp.getkey("s"): ud = -speed

        if kp.getkey("a"): yv = -speed
        elif kp.getkey("d"): yv = speed

        if kp.getkey("q"): yv = drone.land(); time.sleep(3)
        if kp.getkey("e"): yv = drone.takeoff()

        if kp.getkey("z"): 
              cv2.imwrite(f"Resourses/Images/{time.time()}.jpg",img) #Todo Save Image
              time.sleep(0.3)

        return [lr, fb, ud, yv]

    

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(360,240)) # Todo Resize the image 
    cv2.imshow("Drone Image",img)
    cv2.waitKey(1) #The Frame will shutdown immediately if we don't write this code