import cv2
import numpy as np
from matplotlib import pyplot as plt

myList1 = ['A','B','C','D','del','E','F','G','H','I','J','K','L','M','N','nothing','O','P','Q','R','S','space','T','U','V','W','X','Y','Z']
myList=[['A',242],['B',258],['C',247],['D',147],['E',243],['F',226],['G',241],['H',116],['I',179],['K',245],['L',182],['M',235],['N',237],['O',229],['P',234],['Q',216],['R',210],['S',229],['T',216],['U',135],['V',122],['W',128],['X',201],['Y',251]]

for j in range(len(myList)):
    for i in range(1,myList[j][1]+1):
        img = cv2.imread('output5/'+str(myList[j][0])+'/G'+str(myList[j][0])+str(i)+'.jpg',0) 
        canny = cv2.Canny(img ,100,200)
        cv2.imwrite('output6/'+str(myList[j][0])+'/C'+str(myList[j][0])+str(i)+'.jpg',canny)
    print(str(myList[j][0])+ ' done')



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