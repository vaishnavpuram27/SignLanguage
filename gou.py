# convert image to YCrCb from RGB
import numpy as np
import cv2

def grey(letter,upper_limt):
    for i in range(1,upper_limt+1):
        img = cv2.imread('New/'+letter+'/'+letter+str(i)+'.jpg',0) 
        # grey= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('output5/'+letter+'/G'+str(letter)+str(i)+'.jpg',img)
    print(letter+ ' done')

myList=[['A',242],['B',258],['C',247],['D',147],['E',243],['F',226],['G',241],['H',116],['I',179],['K',245],['L',182],['M',235],['N',237],['O',229],['P',234],['Q',216],['R',210],['S',229],['T',216],['U',135],['V',122],['W',128],['X',201],['Y',251]]




