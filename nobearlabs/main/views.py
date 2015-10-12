# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView,View
from django.contrib import messages
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.contrib import auth  # For login
from django.contrib.auth.models import User

from util import forms
#import settings

class MainView(TemplateView):
    template_name = 'main/main.html'
    def get(self, request, *args, **kwargs):
	data = {'a':1,'b':2,'c':123}
        return render(self.request,self.template_name,data)    

class HomePageView(TemplateView):
    template_name = 'homepage.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ThankyouView(TemplateView):
    template_name = 'thankyou.html'

class ChangelogView(TemplateView):
    template_name = 'changelog.html'


