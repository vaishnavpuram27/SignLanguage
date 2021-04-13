import cv2 
import numpy as np

img = cv2.imread('watch.jpg')

ret , thres  = cv2.threshold(img,10,255,cv2.THRESH_BINARY)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
ret2 , thres2  = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
gaus  = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('orginal',img)
cv2.imshow('threshold',thres)
cv2.imshow('threshold2',thres2)
cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()