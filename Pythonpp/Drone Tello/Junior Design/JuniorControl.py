from djitellopy import Tello
import cv2
import time 

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    img = frame_read.frame
    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC
        break
    elif key == ord('w'):
        tello.move_forward(50)
    elif key == ord('s'):
        tello.move_back(50)
    elif key == ord('a'):
        tello.move_left(50)
    elif key == ord('d'):
        tello.move_right(50)
    elif key == ord('e'):
        tello.rotate_clockwise(50)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(50)
    elif key == ord('r'):
        tello.move_up(50)
    elif key == ord('f'):
        tello.move_down(50)
        
tello.land()
cv2.destroyAllWindows()