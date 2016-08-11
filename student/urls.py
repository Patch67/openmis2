from django.conf.urls import url
from . import views

app_name = "student"

urlpatterns = [
    # /student/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /student/232/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /student/123/update/
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateView.as_view(), name='update'),
    # /student/add
    url(r'student/add/$', views.StudentCreate.as_view(), name='student-create'),
    # /qualification/
    url(r'qualification/$', views.QualificationIndex.as_view(), name='qualification-index'),
    # /qualification/add
    url(r'qualification/add/$', views.QualificationCreate.as_view(), name='qualification-create'),
]
