import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # size of width
    width = int(cap.get(3))
    # size of height
    height = int(cap.get(4))
   
    # drawing a rectangle on an iamge
    # (100, 100) is the center coordinate
    # (200, 300) is the width and height of rectangle
    # (0, 0, 255) is the color 
    # 8 is the thickness of the rectangle
    image = cv2.rectangle(frame, (100, 100), (200, 300), (255, 0, 0), 8)
    image = cv2.rectangle(image, (width//4,3*(height//4)), (width//2, height//2),(0,0,255),8)
    
    
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()