from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from gpx.models import GpxObject

class MapView(TemplateView):
    template_name = 'map/map.html'

    def get(self, request):
        gpxobjs = GpxObject.objects.all()
        args = {'nbar': 'map'}
        return render(request, self.template_name, args)


class SpecificMapView(TemplateView):

    template_name = 'map/map.html'
    def get(self, request, gpxid):
        gpxObj = GpxObject.objects.get(pk=gpxid)
        args = {'gpxObj': gpxObj, 'specific': True, 'nbar': 'map'}
        return render(request, self.template_name, args)