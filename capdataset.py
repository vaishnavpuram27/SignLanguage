import cv2 
import os
import time

IMAGES_PATH = 'E:/sem 5 proj_labs/mini project/project/collectedimages' 

labels=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Nothing']
number_img = 1

for label in labels:
    !mkdir {'E:\sem 5 proj_labs\mini project\project\collectedimages\\'+label}
    cap=cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(10)
    for imgnum in range(number_img):
        _, frame=cap.read()
        frame = cv2.flip(frame, 1)
        x1 = int(0.5*frame.shape[1])
        y1 = 10
        x2 = frame.shape[1]-10
        y2 = int(0.5*frame.shape[1])
         # The increment/decrement by 1 is to compensate for the bounding box
        cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
        roi = frame[y1:y2, x1:x2]

        imgname = os.path.join(IMAGES_PATH,label,label+'_'+'{}.jpg'.format(str(imgnum)))
        cv2.imwrite(imgname, roi)
        cv2.imshow('roi',roi)
        cv2.imshow('frame',frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

cv2.destroyAllWindows()
    