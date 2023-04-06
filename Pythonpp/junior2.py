from djitellopy import Tello

tello = Tello()
tello.connect()

tello.takeoff()
tello.move_left(20)
tello.move_right(20)
tello.move_back(20)  # Move back by 50 cm
tello.move_forward(20) # Move forward by 50 cm
tello.rotate_clockwise(360)
