# convert image to YCrCb from RGB
import numpy as np
import cv2

myList = ['A','B','C','D','del','E','F','G','H','I','J','K','L','M','N','nothing','O','P','Q','R','S','space','T','U','V','W','X','Y','Z']

for j in range(len(myList)):
    for i in range(1,3001):
        img = cv2.imread('input/'+str(myList[j])+'/'+str(myList[j])+str(i)+'.jpg') 
        grey= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('output2/'+str(myList[j])+'/G'+str(myList[j])+str(i)+'.png',grey)
    print(str(myList[j])+ ' done')


