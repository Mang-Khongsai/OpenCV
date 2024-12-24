import cv2 
import numpy as np 

img = cv2.imread('./assets/chessboard.jpg')
#img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# img is source image
# 100 is number of corners
# 0.01 is minimum quality
# 10 is minimum euclidean distance
# (x1, y1), (x2, y2)
# sqrt((x2 - x1)^2 + (y2 - y1)^2)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10 )
corners = np.int32(corners)
# print(corners)

for corner in corners:
    # ravel() [[x, y]] --> [x, y]
    # [[x,y], [z, a]] --> [x, y, z, a]
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i,0]) # corners[i][0]
        corner2 = tuple(corners[j,0]) # corners[j][0]
        color = tuple(map(lambda x: int(x),np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('chess board',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

