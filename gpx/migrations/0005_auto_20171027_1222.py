# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpx', '0004_auto_20171026_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpxobject',
            name='xmlfile',
            field=models.FileField(blank=True, null=True, upload_to='xml/'),
        ),
    ]
