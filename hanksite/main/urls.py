from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'hanksite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^index/$', 'main.views.index'),    
]
