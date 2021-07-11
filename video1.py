import cv2
import numpy as np
import math
import joblib
import tensorflow as tf
from tensorflow import keras
cap = cv2.VideoCapture(1)
# mo = joblib.load('random_model_blur')
model  = keras.models.load_model("cnn_model_cannyh5.h5")
def prediction(img,model):
    myList = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
    new_img = cv2.resize(img,(200,150))
    new_img=new_img.reshape(1,150,200)
    prediction = model.predict(new_img)  
    score = tf.nn.softmax(prediction)
    print(str(myList[np.argmax(score)]))
    return str(myList[np.argmax(score)])
     
while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Got this from collect-data.py
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    
    # Resizing the ROI so it can be fed to the model for prediction
    roi = cv2.resize(roi, (200, 150)) 
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, test_image = cv2.threshold(roi, 200, 150, cv2.THRESH_BINARY_INV)
    canny = cv2.Canny(roi,50,150)
    cv2.imshow("canny1",canny)
    # canny  = cv2.GaussianBlur(canny,(5,5),0)
    
    # cv2.imshow("test", test_image)
    # cv2.imshow("canny",canny)
    result = prediction(canny,model)
    cv2.putText(frame,result, (10, 120), cv2.FONT_HERSHEY_PLAIN, 5, (0,255,255), 5) 
    cv2.imshow("Frame", frame)

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break

     
cap.release()
cv2.destroyAllWindows()