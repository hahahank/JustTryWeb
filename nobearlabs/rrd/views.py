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
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import os,time

from util import forms
import rrdManager
import settings
#import settings
TEMP_DETAIL = "product/detail.html"
TEMP_MAIN = 'product/main.html'
TEMP_INSERT = 'product/insert.html'

rrdManager = rrdManager.RrdManager()
class RrdMainView(TemplateView):
    template_name = 'rrd/main.html'
    def get(self, request, *args, **kwargs):
        return render(self.request,self.template_name,{})    

from rest_framework.views import APIView
from rest_framework.response import Response


class RrdFatch(APIView):
  def get(self, request, format=None):
#    print "rest >> request: ",request," ,format: ",format
    try:
	print "= = ",request.GET['start_time']
    except:
	print "not get start time"
    # TODO : 需要增加條件
    result = rrdManager.getData()
# Get result: ( (1438070400, 1438250400, 7200),
#	        ('test',),
#	        [(None,), (None,), (None,), (None,), (None,), (None,), (None,), (None,), (None,), (None,), (None,), (None,), 
#	         (None,), (None,), (None,), (45,), ]
# 	      ) 
    dsStartTime = result[0][0]
    dsStep = result[0][2]
    dsData=result[2]
    
    tarFormat = []
    i = 0
    for v in dsData:
	ptime = dsStartTime + dsStep*i
	if(v[0]==None):
	    pvalue = 0
 	else:
	    pvalue = int(v[0])
        point = {'time':time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ptime)),'value':pvalue}
	tarFormat.append(point)
        i+=1
    # TARGET FORMAT : [{'time':"111",'value':"222"},]
    # time to dormat string :time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
    
 #   print "get result ",tarFormat
    return Response(tarFormat)

