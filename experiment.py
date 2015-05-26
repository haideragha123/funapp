import numpy as np
import cv2
import os.path
from PIL import Image

face_cascade = cv2.CascadeClassifier('C:\opencv\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\opencv\data\haarcascades\haarcascade_eye.xml')
imgfolder = 'ladies/'

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
	
	img = cv2.imread('ladies/' + imgo)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.2, 5)
	idx = 0
	for (x,y,w,h) in faces:
		
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		
		cv2.imwrite('pictures/0/' + str(num + idx) + '.jpg', roi_color)
		idx +=1

	num += len(faces)

cv2.destroyAllWindows()


def cv2pil(cv_im):
    # Convert the cv image to a PIL image
    return Image.fromstring("L", cv.GetSize(cv_im), cv_im.tostring())
