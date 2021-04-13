import cv2
import numpy as np
import matplotlib.pyplot as plt
myList = ['A','B','C','D','del','E','F','G','H','I','J','K','L','M','N','nothing','O','P','Q','R','S','space','T','U','V','W','X','Y','Z']
for j in range(len(myList)):
    for i in range(1,3001):
        img = cv2.imread('input/'+str(myList[j])+'/'+str(myList[j])+str(i)+'.jpg')
        img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret , mask  = cv2.threshold(img2gray,70,255,cv2.THRESH_BINARY_INV)    
        img_fg = cv2.bitwise_and(img,img,mask=mask)
        img_fg = cv2.cvtColor(img_fg,cv2.COLOR_BGR2GRAY)
        cv2.imwrite('output/'+str(myList[j])+'/G'+str(myList[j])+str(i)+'.png',img_fg)
    print(str(myList[j])+ ' done')

# DON'T USE THIS , ITS JUST FOR REFERNECE PURPOSE    
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
# cv2 -> BGR    matplotlib ->RGB
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img,cmap='gray', interpolation='bicubic')
# plt.plot([50,100],[80,100],'c',linewidth=5)
# plt.show()
    
# img = cv2.imread('fore.png')
# img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret , mask  = cv2.threshold(img2gray,150,255,cv2.THRESH_BINARY_INV)    
# img_fg = cv2.bitwise_and(img,img,mask=mask)
# img_fg = cv2.cvtColor(img_fg,cv2.COLOR_BGR2GRAY)
# cv2.imwrite('fore1.png',img_fg)