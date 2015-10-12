
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response,render

from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView

import vdoManager

manager = vdoManager.vdoManager()
class DsVideoView(TemplateView):
    template_name = 'ds/video.html'

class DsMainView(TemplateView):
    template_name = 'ds/main.html'

class ApiGetView(APIView):
    def get(self, request, format=None):
        dataJson = {}
        #for k,v in  request.data.items():
        #    print "AJAX API: K&V:",k,v
        dataJson = manager.getListByName()
        dataJson = sorted(dataJson.items())
        #print "request",request.data
        return Response({"success": True, "data":dataJson })

