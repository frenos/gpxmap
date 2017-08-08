from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.MapView.as_view(), name='Map'),
    url(r'^(?P<gpxid>\d+)$', views.SpecificMapView.as_view(), name='specificMap'),
]