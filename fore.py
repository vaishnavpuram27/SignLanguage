import cv2
import numpy as np
import matplotlib.pyplot as plt

# for i in range(1,3001):
# img = cv2.imread('input/A/A'+str(1)+'.jpg')
# mask = np.zeros(img.shape[:2],np.uint8)

# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)

# rect = (10,5,160,190)
# cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
# mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

# img= img*mask2[:,:,np.newaxis]
# # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# plt.imshow(img)
# # plt.imshow(img2)

# plt.colorbar()
# plt.show()
# cv2.imwrite('output/A/GA'+str(i)+'.png',img)
# print(str(i) +" completed")



img = cv2.imread('001.jpg')
img2 = cv2.imread('066.jpg')

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (100,70,520,450)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

img= img*mask2[:,:,np.newaxis]
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(img)
#  plt.imshow(img2)

plt.colorbar()
plt.show()