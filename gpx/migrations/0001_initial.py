# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 11:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GpxObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('file', models.FileField(null=True, upload_to='gpx/')),
                ('uploadDate', models.DateTimeField(default=datetime.datetime(2017, 8, 8, 11, 13, 43, 601918, tzinfo=utc))),
            ],
        ),
    ]
