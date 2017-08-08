import os
from django.core.files import File
from django.db import models
from django.utils import timezone
from .tasks import plotFiles
# Create your models here.

class GpxObject(models.Model):
    name = models.CharField(max_length=512)
    file = models.FileField(upload_to='gpx/', null=True)
    accuracygraph = models.ImageField(upload_to='accuracy/', null=True)
    speedgraph = models.ImageField(upload_to='speed/', null=True)
    uploadDate = models.DateTimeField(auto_now_add=True)

    def generateDiagrams(self):
        speeddiag = plotFiles(self.file.path, 'speed', 'speed_%s.jpg'%(self.pk))
        with open('speed_%s.jpg'%(self.pk), "r", encoding='utf-8') as originalFile:
            self.speedgraph.save('speed_%s.jpg'%(self.pk), File(originalFile),save=True)
        os.remove('speed_%s.jpg'%(self.pk))
        accuracydiag = plotFiles(self.file.path, 'accuracy', 'accuracy_%s.jpg'%(self.pk))
        with open('accuracy_%s.jpg'%(self.pk), "r") as originalFile:
            self.accuracygraph.save('accuracy_%s.jpg'%(self.pk), File(originalFile),save=True)
        os.remove('accuracy_%s.jpg'%(self.pk))