from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.GpxIndex.as_view(), name='Gpxlist'),
    url(r'^add$', views.GpxAdd.as_view(), name='Gpxadd'),
]