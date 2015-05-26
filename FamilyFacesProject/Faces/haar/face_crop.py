import numpy as np
import cv2
import os.path
from PIL import Image

def face_crop(image):

    face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('cascades\haarcascade_eye.xml')
    #imgfolder = 'test/'
    results_folder = 'temp/'

    idx = 0
    #for imgo in os.listdir(imgfolder):

    img = cv2.imread(os.path.join(image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #gray = cv2.equalizeHist(gray)
    
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    idx = 0
    print len(faces)
    for (x,y,w,h) in faces:
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        cv2.imwrite(results_folder + str(idx) + '.jpg', roi_color)
        idx +=1
    	
    cv2.destroyAllWindows()
    
face_crop(os.path.join('1.jpg'))