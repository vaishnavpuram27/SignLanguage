import cv2
import numpy as np
from matplotlib import pyplot as plt

myList = ['A','B','C','D','del','E','F','G','H','I','J','K','L','M','N','nothing','O','P','Q','R','S','space','T','U','V','W','X','Y','Z']

for j in range(len(myList)):
    for i in range(1,3001):
        img = cv2.imread('output2/'+str(myList[j])+'/G'+str(myList[j])+str(i)+'.png',0) 
        canny = cv2.Canny(img ,100,200)
        cv2.imwrite('output3/'+str(myList[j])+'/C'+str(myList[j])+str(i)+'.png',canny)
    print(str(myList[j])+ ' done')



# img = cv2.imread("GA256.png",0)
# # lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
# # lap = np.uint8(np.absolute(lap))
# # sobleX = cv2.Sobel(img,cv2.CV_64F,1,0)
# # sobleY = cv2.Sobel(img,cv2.CV_64F,0,1)
# canny = cv2.Canny(img ,100,200)
# # sobleX = np.uint8(np.absolute(sobleX))
# # sobleY = np.uint8(np.absolute(sobleY))
# # sobleCombined = cv2.bitwise_or(sobleX,sobleY)
# # titles = ['image','Laplacian','sobleX','sobleY','sobleCombined','canny']
# titles=['image','canny']
# # images = [img,lap,sobleX,sobleY,sobleCombined,canny]
# images = [img,canny]
# for i in range(2):
#     plt.subplot(1,2,i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# cv2.imwrite('CA487.png',canny)
# plt.show()