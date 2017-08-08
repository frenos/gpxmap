from django.contrib import admin
from .models import GpxObject

# Register your models here.
class gpxObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')

admin.site.register(GpxObject, gpxObjectAdmin)