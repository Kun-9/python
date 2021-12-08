import cv2

img = cv2.imread('picture.jpeg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img, (50,50))
img3 = img[128:,:128]
img4 = cv2.blur(img, (15, 15))

cv2.imshow('origianl', img)
cv2.imshow('resized', img2)
cv2.imshow('resized2', img3)
cv2.imshow('resized2', img4)

cv2.waitKey()
cv2.destroyAllWindows()
