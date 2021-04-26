import pandas as pd 
import numpy as np
import cv2
flatten_img=[]
myList=[['A',242],['B',258],['C',247],['D',147],['E',243],['F',226],['G',241],['H',116],['I',179],['K',245],['L',182],['M',235],['N',237],['O',229],['P',234],['Q',216],['R',210],['S',229],['T',216],['U',135],['V',122],['W',128],['X',201],['Y',251]]

for j in range(len(myList)):
    for i in range(1,myList[j][1]+1):
        img = cv2.imread('gaussian_blur_new/'+str(myList[j][0])+'/gb'+str(myList[j][0])+str(i)+'.jpg',0) 
        canny_array = np.array(img)
        canny_flat = canny_array.flatten()
        flatten_img.append(canny_flat)
    print(str(myList[j][0])+ ' done')
flatten_img = np.array(flatten_img)
print(flatten_img.shape)
columns=[]
for i in range(1,30001):
    columns.append("px{}".format(i))
df = pd.DataFrame(data=flatten_img,columns=columns)
print(df.head())
df.to_csv('dataset2.csv',index=False)
# arr = [[1,2],[1,2]]
# print(arr.shape)

        