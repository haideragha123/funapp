# import facerec modules
from Faces.haar.facerec.feature import Fisherfaces, SpatialHistogram, Identity
from Faces.haar.facerec.distance import EuclideanDistance, ChiSquareDistance
from Faces.haar.facerec.classifier import NearestNeighbor
from Faces.haar.facerec.model import PredictableModel
from Faces.haar.facerec.validation import KFoldCrossValidation
from Faces.haar.facerec.visual import subplot
from Faces.haar.facerec.util import minmax_normalize
from Faces.haar.facerec.serialization import save_model, load_model
# import numpy, matplotlib and logging
import numpy as np
# try to import the PIL Image module
try:
    from PIL import Image
except ImportError:
    import Image
import logging
from Faces.haar.facerec.lbp import LPQ, ExtendedLBP

from Faces.models import Person

from django.conf import settings
from django.core.files import File

import sys, os

def read_images(path, sz=(100,100)):

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
					y.append(c)
				except IOError, (errno, strerror):
					print "I/O error({0}): {1}".format(errno, strerror)
				except:
					print "Unexpected error:", sys.exc_info()[0]
					raise
            c = c+1
    return [X,y]
	


def testresults(testdir,orig_img):
	model = load_model(settings.MEDIA_ROOT + '/genderclass.pkl')
	for pic in os.listdir(testdir):
		im = Image.open(os.path.join(testdir,pic))
		im = im.convert("L")
		im = im.resize((100,100), Image.ANTIALIAS)
		f = open(os.path.join(testdir,pic), 'r')
		cropped_image_file = File(f)
		predicted_label = model.predict(np.asarray(im,dtype=np.uint8))[0]
		if (predicted_label == 0):
			print "Found a female"
			p = Person(original_image=orig_img, cropped_image=cropped_image_file, gender='F')
			p.save()
		else :
			print "Found a male"
			p = Person(original_image=orig_img, cropped_image=cropped_image_file, gender='M')
			p.save()
		f.close()