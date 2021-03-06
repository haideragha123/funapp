from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Picture
from .models import Person
from .forms import SubmitPictureForm
from .run import *

def index(request):
	if request.method == 'POST':
		form = SubmitPictureForm(request.POST, request.FILES)
		if form.is_valid():
			p = Picture(image_file = form.cleaned_data['imagefile'], submit_date = timezone.now())
			p.save()
			run(p)
			return HttpResponseRedirect(reverse('success',args=(p.id,)))
	else :
		form = SubmitPictureForm()
	return render(request, 'Faces/index.html', {'form' : form})

def about(request):
	return render(request, 'Faces/about.html', {})

def success(request, picture_id):
	picture = get_object_or_404(Picture, pk=picture_id)
	cropped_people = Person.objects.filter(original_image=picture)
	print cropped_people
	return render(request, 'Faces/success.html', {
		'picture_url' : picture.image_file.url,
		'cropped_people' : cropped_people
		})