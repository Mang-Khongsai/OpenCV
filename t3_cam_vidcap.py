import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # size of width
    width = int(cap.get(3))
    # size of height
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    
    # (0, 0) is the starting coordinate of a frame
    # (0, 0) is the top most left position
    # (width, height) ending coordinate of a frame
    # width is topmost right
    # height is bottommost left
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    
    # fitting resize video in top left
    image[:height//2, :width//2] = smaller_frame
    # fitting resize video in bottom left
    image[height//2:, :width//2] = smaller_frame
    # fitting resize video in top right
    image[:height//2, width//2:] = smaller_frame
    # fitting resize video in bottom right
    image[height//2:, width//2:] = smaller_frame
    
    
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()