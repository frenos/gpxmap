# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpx', '0003_gpxobject_xmlfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpxobject',
            name='accuracygraph',
        ),
        migrations.RemoveField(
            model_name='gpxobject',
            name='speedgraph',
        ),
    ]
