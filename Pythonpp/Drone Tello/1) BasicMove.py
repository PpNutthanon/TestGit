from djitellopy import tello
from time import sleep

drone = tello.Tello() # Create Tello object
drone.connect()
print(drone.get_battery()) # Check Tello's battery

#? Basic Movements
drone.takeoff()
drone.send_rc_control(0,-50,0,0) #X,Y,Z,Rotate
sleep(2)
drone.send_rc_control(0,0,0,30)
sleep(2)
drone.send_rc_control(0,0,0,0)
drone.land()

