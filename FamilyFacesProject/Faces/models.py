from django.db import models

YOURSELF = 'YOU'
BROTHER = 'BRO'
SISTER = 'SIS'
FATHER = 'DAD'
MOTHER = 'MOM'
SON = 'SON'
DAUGHTER = 'DAU'
GRANDMOTHER = 'GRM'
GRANDFATHER = 'GRF'
GRANDSON = 'GRS'
GRANDDAUGHTER = 'GRD'
OTHER = 'OTH'
RELATION_TYPE_CHOICES = (
	(YOURSELF, 'yourself'),
	(BROTHER, 'brother'),
	(SISTER, 'sister'),
	(FATHER, 'father'),
	(MOTHER, 'mother'),
	(SON, 'son'),
	(DAUGHTER, 'daughter'),
	(GRANDMOTHER, 'grandmother'),
	(GRANDFATHER, 'grandfather'),
	(GRANDSON, 'grandson'),
	(GRANDDAUGHTER, 'granddaughter'),
	(OTHER, 'other'),
)

MALE = 'M'
FEMALE = 'F'
GENDER_CHOICES = (
	(MALE, 'male'),
	(FEMALE, 'female'),
)

class Picture(models.Model):
	
	image_file = models.ImageField(upload_to='Faces/original')
	submit_date = models.DateTimeField()

	def __str__(self):
		return self.submit_date.strftime("%Y-%m-%d %H:%M")

class Person(models.Model):

	original_image = models.ForeignKey(Picture)
	cropped_image = models.ImageField(upload_to='Faces/cropped')
	relation_type = models.CharField(max_length=3,
                                      choices=RELATION_TYPE_CHOICES,
                                      default=OTHER)
	reference_person = models.OneToOneField('self', null=True)
	age = models.IntegerField()
	gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default=MALE)

	def __str__(self):
		return self.relation_type