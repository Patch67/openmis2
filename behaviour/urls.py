from django.conf.urls import url
from . import views

app_name="behaviour"

urlpatterns = [
    url(r'^(?P<behaviour_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]
