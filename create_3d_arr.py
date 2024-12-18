import numpy as np 
import cv2 
shape = (800, 600, 3)

color = np.zeros(shape)

print(color)
print()
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            if i<=200 or (i>400 and i<600):
                # this will return black color
                color[i,j,k] = np.random.randint(0,1)
            else:
                # this will return white color
                color[i,j,k] = np.random.randint(255,256)
    
            
cv2.imshow("color", color)
cv2.waitKey()
cv2.destroyAllWindows()