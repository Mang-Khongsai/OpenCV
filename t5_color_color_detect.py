import numpy as  np 
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) # measure the width of the frame
    height = int(cap.get(4)) # measures the height of the frame
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue  = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('frame', result)
    cv2.imshow('mash', mask)
    if cv2.waitKey(1) == ord('q'):
        break 
        
cap.release()
cv2.destroyAllWindows()