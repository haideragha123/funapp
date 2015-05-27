import numpy as np
import cv2
import os.path
from PIL import Image

from django.conf import settings

def face_crop(image_path, temp_path):

    CASCADE_PATH = settings.MEDIA_ROOT +'/cascades/haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
    #eye_cascade = cv2.CascadeClassifier('cascades\haarcascade_eye.xml')
    #imgfolder = 'test/'
    results_folder = temp_path + '/'
    print image_path

    idx = 0
    #for imgo in os.listdir(imgfolder):

    img = cv2.imread(image_path)
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
