# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cropped_image', models.ImageField(upload_to=b'')),
                ('relation_type', models.CharField(default=b'OTH', max_length=3, choices=[(b'YOU', b'yourself'), (b'BRO', b'brother'), (b'SIS', b'sister'), (b'DAD', b'father'), (b'MOM', b'mother'), (b'SON', b'son'), (b'DAU', b'daughter'), (b'GRM', b'grandmother'), (b'GRF', b'grandfather'), (b'GRS', b'grandson'), (b'GRD', b'granddaughter'), (b'OTH', b'other')])),
                ('age', models.IntegerField()),
                ('gender', models.CharField(default=b'M', max_length=3, choices=[(b'M', b'male'), (b'F', b'female')])),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(upload_to=b'')),
                ('submit_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='original_image',
            field=models.ForeignKey(to='Faces.Picture'),
        ),
        migrations.AddField(
            model_name='person',
            name='reference_person',
            field=models.OneToOneField(null=True, to='Faces.Person'),
        ),
    ]
