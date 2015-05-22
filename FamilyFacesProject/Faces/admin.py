from django.contrib import admin

from .models import Picture, Person

admin.site.register(Person)
admin.site.register(Picture)