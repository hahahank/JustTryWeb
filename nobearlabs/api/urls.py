from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
 
urlpatterns = patterns('',
  url(r'^get/$', views.ApiGet.as_view()),
)
 

urlpatterns = format_suffix_patterns(urlpatterns)
