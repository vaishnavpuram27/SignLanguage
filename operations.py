import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)



img[55,55] = [255,255,255]
px = img[55,55]

# roi = Region of image
# roi =  img[100:150, 100:150]


img[100:150, 100:150] = [255,255,255]

watch_face = img[300:700,300:700]

img[0:367,0:400] = watch_face
cv2.imshow('watch.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

