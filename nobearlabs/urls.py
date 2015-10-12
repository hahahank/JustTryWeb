# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include
from django.conf.urls import patterns, url
from django.contrib.auth.models import User
from django.contrib import admin
admin.autodiscover()
#from django.contrib.sitemaps.views import sitemap

from rest_framework import routers
import settings
from main.views import *
from users.views import *

# BLOG +++++++++++++++
import zinnia
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}



urlpatterns = patterns('',
#    'django.contrib.sitemaps.views',
    # media
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',   {'document_root': settings.MEDIA_ROOT}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',      {'document_root': settings.STATIC_ROOT+"js/"}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',       {'document_root': settings.STATIC_ROOT+"css/"}),

    # Social Auth
    url(r'', include('social_auth.urls')),

    # MY apps 
    (r'^main/', include('main.urls')),
    (r'^demo/', include('demo.urls')),
    (r'^product/', include('product.urls')),
    (r'^machine/', include('machine.urls')),  
    (r'^api/', include('api.urls')),
    (r'^rrd/', include('rrd.urls')),
    (r'^users/',include('users.urls'))  ,
    (r'^ds/',include('ds.urls'))  ,
    #  OTHER APP
#    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
#    url(r'^comments/', include('django_comments.urls')),

    # web main function
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', HomePageView.as_view(), name='homepage'),
     url(r'^login$', LoginView.as_view(), name='login'),
     url(r'^logout$', LogoutView.as_view(), name='logout'),
#     url(r'^signup$', SignUpView.as_view(), name='signup'),
     url(r'^createuser$',CreateUserView.as_view(), name='createuser'),
     url(r'^about$', AboutView.as_view(), name='about'),	
     url(r'^thankyou$',ThankyouView.as_view(), name='thankyou'),
     url(r'^changelog$',ChangelogView.as_view(),name='changelog'),
)
urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',        {'sitemaps': sitemaps}),
)

