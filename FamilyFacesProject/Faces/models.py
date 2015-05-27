from django.db import models

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
	gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default=MALE)