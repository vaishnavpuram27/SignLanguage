import numpy as np
import cv2

img = cv2.imread('A1.jpg',cv2.IMREAD_COLOR)

cv2.line(img , (0,0) , (150,150) , (0,0,255),5)
cv2.rectangle(img,(15,25) , (150,100),(0,255,0),5)
cv2.circle(img,(100,125) ,20,(255,0,0),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
# pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV' , (0,170) , font ,1,(0,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()