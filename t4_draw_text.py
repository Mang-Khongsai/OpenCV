import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # size of width
    width = int(cap.get(3))
    # size of height
    height = int(cap.get(4))

    # draw a TEXT
    # 'Code with Tim!' is the text to be displayed or renedered on the screen
    # (200, height-10) bottom left hand corner or center position
    # font and 
    # cv2.LINE_AA is linetype
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(frame, 'Code!',(10, height-10), font, 1, (255, 255, 255), 5, cv2.LINE_AA)
    image = cv2.putText(image, 'with!',(100, height-20), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
    image = cv2.putText(image, 'Tim!',(200, height-30), font, 1, (255, 0, 0), 3, cv2.LINE_AA)
    
    
    
    
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()