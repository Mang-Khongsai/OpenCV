import cv2 
import random

img = cv2.imread('assets/image1.jpg', -1)

# image representation
# for i in range(101,201):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

print(img.shape)

cv2.imshow("Image",img)       
cv2.waitKey(0)
cv2.destroyAllWindows()