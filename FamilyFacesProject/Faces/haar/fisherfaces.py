import sys, os
sys.path.append("../..")
# import facerec modules
from facerec.feature import Fisherfaces, SpatialHistogram, Identity
from facerec.distance import EuclideanDistance, ChiSquareDistance
from facerec.classifier import NearestNeighbor
from facerec.model import PredictableModel
from facerec.validation import KFoldCrossValidation
from facerec.visual import subplot
from facerec.util import minmax_normalize
from facerec.serialization import save_model, load_model
# import numpy, matplotlib and logging
import numpy as np
# try to import the PIL Image module
try:
    from PIL import Image
except ImportError:
    import Image
import logging
from facerec.lbp import LPQ, ExtendedLBP


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
	
def testresults(testdir, model):

    for pic in os.listdir(testdir):

        im = Image.open(os.path.join(testdir,pic))
        im = im.convert("L")
        im = im.resize((100,100), Image.ANTIALIAS)

        predicted_label = model.predict(np.asarray(im,dtype=np.uint8))[0]
        print predicted_label
        

my_model = load_model('genderclass.pkl')
testresults('temp', my_model)
