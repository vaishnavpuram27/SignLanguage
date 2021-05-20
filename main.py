import cv2
import numpy as np
import pandas as pd
import joblib

img = cv2.imread('new1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img,100,200)
canny  = cv2.GaussianBlur(canny,(5,5),0)
# cv2.imshow('canny',canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
canny_array = np.array(canny)
canny_flat = canny_array.flatten()
print(canny_flat.shape)

mo = joblib.load('svm_model_blur')
print(mo.predict([canny_flat]))