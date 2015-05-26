# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faces', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.RemoveField(
            model_name='person',
            name='reference_person',
        ),
        migrations.RemoveField(
            model_name='person',
            name='relation_type',
        ),
        migrations.AlterField(
            model_name='person',
            name='cropped_image',
            field=models.ImageField(upload_to=b'Faces/cropped'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image_file',
            field=models.ImageField(upload_to=b'Faces/original'),
        ),
    ]
