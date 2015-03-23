from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^index/$', 'main.views.index'),                         
  
)
