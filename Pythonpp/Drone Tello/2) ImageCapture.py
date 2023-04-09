from djitellopy import tello
import cv2

drone = tello.Tello() # Create Tello object
drone.connect()
print(drone.get_battery()) # Check Tello's battery

drone.streamon()

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(360,240)) # Todo Resize the image 
    cv2.imshow("Drone Image",img)
    cv2.waitKey() #The Frame will shutdown immediately if we don't write this code

