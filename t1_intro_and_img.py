import cv2 

img = cv2.imread('./image.webp',0)

# resize the image
# img = cv2.resize(img, (400, 400))
img = cv2.resize(img, (0, 0), fx=0.8, fy=1)

# rotate the image 
#img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# save the image in a folder
cv2.imwrite("./save/new_img1.jpg",img)

cv2.imshow('image', img)
cv2.waitKey(0) # wait infinite second until you click any key
cv2.destroyAllWindows() # close the window


