from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView

from .models import GpxObject
from .forms import GpxAddForm

class GpxIndex(TemplateView):
    template_name = 'gpx/gpxlist.html'

    def get(self, request):
        gpxObjs = GpxObject.objects.all()
        args = {'gpxobjs': gpxObjs,  'nbar': 'gpx'}
        return render(request, self.template_name, args)


class GpxAdd(TemplateView):
    template_name = 'gpx/gpxadd.html'

    def get(self, request):
        form = GpxAddForm(initial={'uploadDate': timezone.now()})
        args = {'form': form, 'nbar': 'gpx'}
        return render(request, self.template_name, args)

    def post(self, request):
        form = GpxAddForm(request.POST, request.FILES)
        if form.is_valid():
            savedInstance = form.save()
            #savedInstance.generateDiagrams()
            return redirect('gpx:Gpxlist')
        else:
            args = {'form': form, 'text': 'Form was not valid!', 'status': True, 'nbar': 'gpx'}
        return render(request, self.template_name, args)