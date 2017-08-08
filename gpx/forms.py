from django.forms import ModelForm
from .models import GpxObject
class GpxAddForm(ModelForm):
    class Meta:
        model = GpxObject
        fields = ['name', 'file']
