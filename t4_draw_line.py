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
    
    # drawing a rectangle on an iamge
    # (100, 100) is the center coordinate
    # (200, 300) is the width and height of rectangle
    # (125, 125, 125) is the color 
    # 8 is the thickness of the rectangle
    image = cv2.rectangle(image, (100, 100), (200, 300), (120, 120, 120), 8)
    image = cv2.rectangle(image, (width//4,3*(height//4)), (width//2, height//2),(100,100,100),8)
    
    # circle
    # (400,200) is the starting position/coordinate
    # 80 is the radius
    # (200, 200, 200) is the color
    # -1 is thickness and it will fill the whole shape
    image = cv2.circle(image, (400, 200),80, (200,200,200),-1)
    
    
    # draw a TEXT
    # 'Code with Tim!' is the text to be displayed or renedered on the screen
    # (200, height-10) bottom left hand corner or center position
    # font and 
    # cv2.LINE_AA is linetype
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(image, 'Code with Tim!',(10, height-10), font, 1, (0,0,0), 5, cv2.LINE_AA)
    
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()