from djitellopy import tello
import Keypress as kp
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery)


def getKeyboardInput():
        lr, fb, up, yv, = 0, 0, 0, 0
        speed = 50
        if kp.getkey("LEFT"): lr = -speed
        elif kp.getkey("RIGHT"): lr = speed

        if kp.getkey("Up"): fb = speed
        elif kp.getkey("Down"): fb = -speed

        if kp.getkey("w"): ud = speed
        elif kp.getkey("s"): ud = -speed

        if kp.getkey("a"): yv = speed
        elif kp.getkey("d"): yv = -speed

        if kp.getkey("q"): drone.land()
        if kp.getkey("e"): drone.takeoff()

        return [lr, fb, ud, yv]

    
drone.takeoff()

while True:
        vals = getKeyboardInput()
        drone.send_rc_control(vals[0],vals[0],vals[0],vals[0])
        sleep(0.05)