from django.conf import settings

from Faces.haar.face_crop import *
from Faces.haar.fisherfaces import *


import os, shutil

def run(picture):

	TEMP_PATH = settings.MEDIA_ROOT +'/temp'
	IMAGE_FILE_PATH = settings.BASE_DIR + picture.image_file.url
	face_crop(IMAGE_FILE_PATH, TEMP_PATH)
	testresults(TEMP_PATH,picture)

	for the_file in os.listdir(TEMP_PATH):
		file_path = os.path.join(TEMP_PATH, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			#elif os.path.isdir(file_path): shutil.rmtree(file_path)
		except Exception, e:
			print e