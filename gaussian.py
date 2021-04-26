import cv2
import numpy as np
from matplotlib import pyplot as plt


myList=[['A',242],['B',258],['C',247],['D',147],['E',243],['F',226],['G',241],['H',116],['I',179],['K',245],['L',182],['M',235],['N',237],['O',229],['P',234],['Q',216],['R',210],['S',229],['T',216],['U',135],['V',122],['W',128],['X',201],['Y',251]]

for j in range(len(myList)):
    for i in range(1,myList[j][1]+1):
        img = cv2.imread('canny_new/'+str(myList[j][0])+'/C'+str(myList[j][0])+str(i)+'.jpg',0) 
        gaussian = cv2.GaussianBlur(img,(5,5),0)
        cv2.imwrite('output7/'+str(myList[j][0])+'/gb'+str(myList[j][0])+str(i)+'.jpg',gaussian)
    print(str(myList[j][0])+ ' done')

# img= cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.gray()
# plt.matshow(img)
# canny_array = np.array(img)
# plt.show()
# print(canny_array)
# print(canny_array.shape)
# canny_flat = canny_array.flatten()
# print(canny_flat)
# print(canny_flat.shape)
# plt.imshow(img,'gray')
# plt.title("my")
# plt.xticks([])
# plt.yticks([])




# surf   = cv2.xfeatures2d.SURF_create()
# sift = cv2.SURF_create()
# kp= sift.detect(img,None)
# img = cv2.drawKeypoints(img,kp,None)
# print(kp)
# cv2.imshow("Surf_image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
