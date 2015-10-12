
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import render_to_response,render

from forms import ContactForm, FilesForm, ContactFormSet

import pttTest


pttTestManager = pttTest.PttManager()

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class PttGet(APIView):
    def get(self, request, format=None):
	myList=[]
        myData = pttTestManager.get()
        for b in myData:
  	    idx = b.get("index")
            num = b.get("property1")
            name = b.get("property2").get("text")
            myList.append([idx,name,num])
#	print "PttGet :",myList
        return Response(myList)


class PttDountGet(APIView):
    def get(self, request, format=None):
	result =[]
        myData = pttTestManager.get()
        for b in myData:
            num = b.get("property1")
            name = b.get("property2").get("text")
 #           print name ,num
            result.append({"label":name,"value":num})
        return Response(result)


class ChartView(TemplateView):
    template_name = 'demo/chart.html'
    def get(self, request, *args, **kwargs):
        data = {'a':1,'b':2,'c':123}
        return render(self.request,self.template_name,data)

class MetricsView(TemplateView):
    template_name = 'demo/metrics.html'
    def get(self, request, *args, **kwargs):
        data = {'a':1,'b':2,'c':123}
        return render(self.request,self.template_name,data)

class TablesView(TemplateView):
    template_name = 'demo/tables.html'
    def get(self, request, *args, **kwargs):
        data = {'a':1,'b':2,'c':123}
        return render(self.request,self.template_name,data)

class VideoView(TemplateView):
    template_name = 'demo/video.html'



# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')


class HomePageView(TemplateView):
    template_name = 'demo/home.html'
    print "=home view="
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
	print "-push message-",kwargs
        return context


class DefaultFormsetView(FormView):
    template_name = 'demo/formset.html'
    form_class = ContactFormSet


class DefaultFormView(FormView):
    template_name = 'demo/form.html'
    form_class = ContactForm
    def get_context_data(self, **kwargs):
        context = super(DefaultFormView, self).get_context_data(**kwargs)
        #messages.info(self.request, 'This is a demo of a message.')
	#myDate = self.request.GET.get('date')
        print "-DefaultFormView-",context
	print "-DefaultFormView-",type(context['form']),'-.-'
	if(context['form'].is_bound==True and context['form'].is_valid== True):
            print "=data=",context['form'].cleaned_data['date']
	else:
	    print "Data Error"
        return context


class DefaultFormByFieldView(FormView):
    template_name = 'demo/form_by_field.html'
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = 'demo/form_horizontal.html'
    form_class = ContactForm
    def get_context_data(self, **kwargs):
        context = super(FormHorizontalView, self).get_context_data(**kwargs)
	f = context['form']
        print "-DefaultFormView-",context
        print "-DefaultFormView-",type(f),'-.-'
        if(f.is_bound==True and f.is_valid==True):
            print "=data=",f.cleaned_data['date']
	else :
	    print f.errors
      	    print f.errors.as_data()
            print "Data Error"
        return context



class FormInlineView(FormView):
    template_name = 'demo/form_inline.html'
    form_class = ContactForm


class FormWithFilesView(FormView):
    template_name = 'demo/form_with_files.html'
    form_class = FilesForm

    def get_context_data(self, **kwargs):
	print "file form 3"
        context = super(FormWithFilesView, self).get_context_data(**kwargs)
        context['layout'] = self.request.GET.get('layout', 'vertical')
 	print "=FormWithFilesView=",context
        f = context['form']
        print "-New product View-",context
        print "-New Product View-",type(f),'-.-'
        if(f.errors == None):
            print "0 ",f.is_bound,f.is_valid,f.cleaned_data
            print "1 ",f.errors
            print "2 ",f.errors.as_data()
            print "3 Data Error"
        else:
            print "Get Context  OK"
            if(f.is_bound == True):
                print "Get data :",f.cleaned_data




	#return HttpResponseRedirect('/')
        return context
    def form_valid(self, form):
	print "file form 1"
	result = self.get_context_data(form=form)

    def get_initial(self):
	print "file form 2",fieldfile
#	result = self.get_context_data(form=form)
        return {            'file4': fieldfile,        }
#	return HttpResponseRedirect('/')

class PaginationView(TemplateView):
    template_name = 'demo/pagination.html'

    def get_context_data(self, **kwargs):
	print "=PaginationView=",kwargs
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(10000):
            lines.append('Line %s' % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context


class MiscView(TemplateView):
    template_name = 'demo/misc.html'

def voteView(request):
    template_name = 'demo/vote.html'
    vote_id = request.GET.get('id')
#    LOGGER.info("Show product detail: "+str(product_id))
    voteInfo = {"id":vote_id}
    # TODO : Get product from Product manager
    
    if( vote_id == None):
         return render(request, template_name, {'id': "Not Found"})
    return render(request, template_name, voteInfo)

