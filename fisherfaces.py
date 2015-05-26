import sys, os
sys.path.append("../..")
# import facerec modules
from facerec.feature import Fisherfaces
from facerec.distance import EuclideanDistance
from facerec.classifier import NearestNeighbor
from facerec.model import PredictableModel
from facerec.validation import KFoldCrossValidation
from facerec.visual import subplot
from facerec.util import minmax_normalize
# import numpy, matplotlib and logging
import numpy as np
from PIL import Image
import matplotlib.cm as cm
import logging


model = PredictableModel(Fisherfaces(), NearestNeighbor())
def read_images(path, sz=(60,60)):

    c = 0
    X,y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
				try:
					im = Image.open(os.path.join(subject_path, filename))
					#im = cv2pil(img)
					im = im.convert("L")
					# resize to given size (if given)
					if (sz is not None):
						im = im.resize(sz, Image.ANTIALIAS)
					#im.show()
					X.append(np.asarray(im, dtype=np.uint8))
					y.append(subdirname)
				except IOError, (errno, strerror):
					print "I/O error({0}): {1}".format(errno, strerror)
				except:
					print "Unexpected error:", sys.exc_info()[0]
					raise
		
    return [X,y]
	
[X,y] = read_images("pictures/")


print len(y)
print len(X)	
model.compute(X,y)

#model.predict('pictures/0/2.jpg')