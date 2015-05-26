import numpy as np
import cv2
import os.path
from PIL import Image

def face_crop():

    face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('cascades\haarcascade_eye.xml')
    imgfolder = 'test/'
    results_folder = 'test_results/'

    fdx = 0
    idx = 0

    if len(imgfolder)<=0:
    	print 'No Images Found'
    	
    #if not os.path.exists('pictures/0/' ):
    	
    #	os.makedirs('cropped/' )
    		
    num = 0
    for imgo in os.listdir(imgfolder):

        fdx +=1
        print imgo

        img = cv2.imread(os.path.join(imgfolder,imgo))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #gray = cv2.equalizeHist(gray)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        idx = 0
        print len(faces)
        for (x,y,w,h) in faces:
            
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            cv2.imwrite(results_folder + str(num + idx) + '.jpg', roi_color)
            idx +=1

        num += len(faces)
    	
    cv2.destroyAllWindows()