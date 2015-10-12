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
import json

import os,time,sys

from util import forms
import settings

from rest_framework.views import APIView
from rest_framework.response import Response

import machineManager

mManager = machineManager.MachineManager()

class MachineMainView(TemplateView):
    template_name = 'machine/main.html'
    def get(self, request, *args, **kwargs):
	infos = mManager.getAllInfo()
	print "[api]",infos
        return render(self.request,self.template_name,infos)


class ApiIpmi(APIView):
    def get(self, request, format=None):
#        print "API IPMI GET"
    	bmc =  request.GET.get('bmc')
	ipmi =  request.GET.get('ipmi')
	print "[API] get ipmi ",bmc,ipmi
	result = mManager.getMachineInfo(bmc,ipmi)
	print "[API] get Ipmi",bmc,ipmi
        return Response(result)

    def post(self, request, format=None):
#	print "API IPMI POST"
	dataJson = {}
	for k,v in  request.data.items():
#	    print "\nKEY :" ,k,type(k)
#	    print "VALUE :",type(v),v.replace("'", '"').replace('None','null')
	    try:
	        vJson = json.loads(v.replace("'", '"').replace('None','null') )
#		print "-.-... ",k,type(k),"+++",vJson,type(vJson)
		dataJson["".join(k)]=vJson
#  	        print "Key OK :",k
 	    except:
		print "ERROR api update ipmi",sys.exc_info()[0]
#		print "Key fail :",k,type(k),"+++",vJson,type(vJson)
#            for i in vJson:
#                print i,"= ="
#                print "\titem:{0} , value:{1} , status:{2}".format(i.get("item"),i.get("value"),i.get("status"))

	result = mManager.updateIpmi(dataJson)
        return Response(result)


