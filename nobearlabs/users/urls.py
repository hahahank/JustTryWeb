# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include
from django.conf.urls import patterns, url
from django.contrib.auth.models import User
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

import settings
from users.views import *


urlpatterns = patterns('',
     url(r'^$', UsersMainView.as_view(), name='users'),
)
