import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # size of width
    width = int(cap.get(3))
    # size of height
    height = int(cap.get(4))

    # circle
    # (400,200) is the starting position/coordinate
    # 80 is the radius
    # (0, 255, 0) is the color
    # -1 is thickness and it will fill the whole shape
    image = cv2.circle(frame, (400, 200),80, (0, 255, 0),-1)
   
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()