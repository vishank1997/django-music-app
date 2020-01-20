from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # for all of music
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<album_id>[0-9])/$', views.detail, name='detail'), #for individual albums
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/favorite/$', views.favorite, name='favorite'),

]
