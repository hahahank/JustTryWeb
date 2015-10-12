# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url
from ds.views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
    url(r'^$', DsMainView.as_view(), name='dsMain'),

    url(r'^video$', DsVideoView.as_view(), name='dsVideo'),

    # API 
    url(r'^get/$',ApiGetView.as_view()),
)



