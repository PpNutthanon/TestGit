from djitellopy import Tello

tello = Tello()
tello.connect()

tello.takeoff()
tello.move_back(100)  # Move back by 50 cm
tello.move_forward(100) # Move forward by 50 cm