import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # size of width
    width = int(cap.get(3))
    # size of height
    height = int(cap.get(4))
    
    # drawing a line on an image
    # (0,0) is the starting coordinate
    # (width, height) is the ending coordinate
    # (255, 255, 255) are color
    # 10 is the thickness of the line
    image = cv2.line(frame, (0, 0), (width, height), (255, 0, 0),10 )
    image = cv2.line(image, (0, height), (width, 0), (0, 255, 0),10 )
    image = cv2.line(image, (width//2, height), (width//2, 0), (0,0,255), 10)
    image = cv2.line(image, (0, height//2), (width, height//2), (255,255,255), 10)
    
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()