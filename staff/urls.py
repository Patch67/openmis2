from django.conf.urls import url
from . import views

app_name = "staff"

urlpatterns = [
    # /staff/
    url(r'^(?P<staff_id>[0-9]+)/$', views.detail, name='detail'),
    # /staff/232/
    url(r'^$', views.index, name='index'),
    # /staff/123/update/
    url(r'^(?P<staff_id>[0-9]+)/update/$', views.detail, name='update'),
]
