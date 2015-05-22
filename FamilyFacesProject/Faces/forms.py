from django import forms

class SubmitPictureForm(forms.Form):
	imagefile = forms.ImageField(label='Please select an image file')