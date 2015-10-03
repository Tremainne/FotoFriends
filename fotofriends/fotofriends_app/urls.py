from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.collection, name='collection'),
    url(r'^(?P<album_id>[0-9]+)/$', views.album, name='album'),
    url(r'^(?P<album_id>[0-9]+)/$', views.paparazzi, name='paparazzi'),
    url(r'^$', views.settings, name='settings')
]
