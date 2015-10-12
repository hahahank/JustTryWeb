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

#from django.core.files.storage import default_storage
#from django.core.files.base import ContentFile
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response



import os
from util import uforms,log,comm
import productManager
import settings
#import settings
TEMP_DETAIL = "product/detail.html"
TEMP_MAIN = 'product/main.html'
TEMP_INSERT = 'product/insert.html'
TEMP_NEW = 'product/new.html'
TEMP_LIST = 'product/list.html'
proManager = productManager.ProductManager()

LOGGER = log.Log('productV').logger
class ProductNewView(FormView):
    template_name = TEMP_INSERT
    form_class = uforms.ProductNewForm

    def get_context_data(self, **kwargs):
        context = super(ProductNewView, self).get_context_data(**kwargs)
        f = context['form']
        #print "-New product View-",context
        if(f.errors == None):
            LOGGER.error("New Data Error")
        else:
            if(f.is_bound == True):
                productInfo = f.cleaned_data
                id = productInfo['productid']
                LOGGER.info("PRO View > Inset New Product "+str(productInfo)+"<<<<<<<<<")
                result =  proManager.insertProduct(id,productInfo)
                if(result == True ):
                    return True
                else:
                    return result[1]
            else:
                LOGGER.debug("No data")
        response = context
        return context

    def form_valid(self, form):
        result = self.get_context_data(form=form)
        if(result==True):
            return HttpResponseRedirect('/product/main')
        else:
            if(type(result)==str):
                messages.warning(self.request,result)
                return HttpResponseRedirect('/product/insert')
            messages.warning(self.request, 'Insert Product Error')
            return HttpResponseRedirect('/product/insert')


class ApiGetView(APIView):
    def get(self, request, format=None):
	dataJson = {}
        #for k,v in  request.data.items():
	#    print "AJAX API: K&V:",k,v
	dataJson = proManager.getProductList()	
	dataJson = sorted(dataJson.items())
	#print "request",request.data
	return Response({"success": True, "data":dataJson })

class ProductMainView(TemplateView):
    template_name = TEMP_MAIN
    def get(self, request, *args, **kwargs):
	productList = proManager.getProductList()
	order = ['server','storage','network','rack','eother']
	all = {}
	byTypes = {}
	for pid,pinfo in productList.items():
	    all[pid] = pinfo
	    for t in pinfo['type']:
 	    	if(byTypes.get(t) == None):
		    byTypes[t] = {}
		    byTypes[t][pid]  = pinfo
	        else:
		    byTypes[t][pid]  = pinfo
	result={"all":all,"types":byTypes,"order":order}
	return render(self.request,self.template_name,result)


class ProductListView(TemplateView):
    template_name = TEMP_LIST
    def get(self, request, *args, **kwargs):
	result = {}
        return render(self.request,self.template_name,result)


class ProductInsertView(FormView):
    template_name = TEMP_INSERT
    form_class = uforms.ProductInsertForm

    def get_context_data(self, **kwargs):
        context = super(ProductInsertView, self).get_context_data(**kwargs)

        f = context['form']
        if(f.errors == None):
            LOGGER.error(" Data Error")
        else:
            if(f.is_bound == True):
		productInfo = f.cleaned_data
                id = productInfo['productid']
	        LOGGER.info( "PRO View > Inset New Product "+str(productInfo)+"<<<<<<<<<")
		result =  proManager.insertProduct(id,productInfo)
		if(result == True ):
		    return True
		else:
		    return result[1]
	    else:
                LOGGER.debug("No data")
        response = context
        return context

    def form_valid(self, form):
        if not self.request.user.is_authenticated():
            messages.info(request, 'Need Login')
            return HttpResponseRedirect('/product/main')

        result = self.get_context_data(form=form)
        if(result==True):
            return HttpResponseRedirect('/product/main')
        else:
     	    if(type(result)==str):
                messages.warning(self.request,result)
		return HttpResponseRedirect('/product/insert')
            messages.warning(self.request, 'Insert Product Error')
            return HttpResponseRedirect('/product/insert')


def product_detail(request):
    template_name = TEMP_DETAIL
#    if not request.user.is_authenticated():
#        messages.info(request, 'Need Login')
#        HttpResponseRedirect('/product/main')
    product_id = request.GET.get('id')
    LOGGER.info("Show product detail: "+str(product_id))
    productInfo = proManager.getPodcuctByID(product_id)
   # print request.user,request.user.is_authenticated()
    # TODO : Get product from Product manager
    if(productInfo == None):
	 return render(request, template_name, {'id': "Not Found"})
    return render(request, template_name, productInfo)

def product_delete(request):
    product_id = request.GET.get('id')
    if not request.user.is_authenticated():
        messages.info(request, 'Need Login')
	HttpResponseRedirect('/product/main')
    user = request.GET.get('name')
    #print request.user
#	LOGGER.warning( "USER IS NOT SUPERUSER")
#	messages.info(request, 'You are not superuser')
#	HttpResponseRedirect('/product/main')
    LOGGER.info("Delete product: "+str(product_id)+" by :"+str(user))
    result = proManager.deleteProduct(product_id)
    if(result):
	messages.info(request, 'Delete Product Success')
	return HttpResponseRedirect('/product/main')
    LOGGER.debug( "delete product error")
    messages.info(request, 'Delete Product Fail')
    return HttpResponseRedirect('/product/main')

