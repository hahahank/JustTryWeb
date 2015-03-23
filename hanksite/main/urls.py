from django.conf.urls import include, url,patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^index/$', 'main.views.index'),                         
#    url(r'^heading/$', 'main.views.heading'),
    url(r'^footing/$', 'main.views.content'),    
    url(r'^menu/$', 'main.views.menu'),
    url(r'^bar/$', 'main.views.bar'),
    url(r'^content/$', 'main.views.content'),
    url(r'^logout/$', 'main.views.logout'),
    url(r'^root/$', 'main.views.root'),        
)
