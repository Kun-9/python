import cv2

img_files = ['picture.jpeg', 'pic.png']

# img = cv2.imread('picture.jpeg',cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image',cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

i = 0
while True :
    img = cv2.imread(img_files[i])
    cv2.imshow('image', img)
    if cv2.waitKey(1000) == 27 :
        break
    i += 1
    if i == len(img_files) :
        i = 0
cv2.destroyAllWindows()
