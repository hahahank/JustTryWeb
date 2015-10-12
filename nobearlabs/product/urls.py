# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'demo.views.home', name='home'),
#     # url(r'^demo/', include('demo.foo.urls')),
#
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = patterns('',
#    url(r'^main$', ProductMainView.as_view(), name='productMain'),
    url(r'^list$', ProductListView.as_view(), name='productList'),
    url(r'^insert$', ProductInsertView.as_view(), name='newProduct'),
    url(r'^detail$', product_detail, name='productdetail'),
    url(r'^delete$', product_delete, name='productdelete'),
    url(r'^new$', ProductNewView.as_view(),name='productnew'),
    url(r'^get/$',ApiGetView.as_view()),
)



