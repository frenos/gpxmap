import os
from django.core.files import File
from django.db import models
from django.utils import timezone
from .tasks import plotFiles
# Create your models here.

class GpxObject(models.Model):
    name = models.CharField(max_length=512)
    file = models.FileField(upload_to='gpx/', null=True)
    xmlfile = models.FileField(upload_to='xml/',null=True, blank=True)
    uploadDate = models.DateTimeField(auto_now_add=True)