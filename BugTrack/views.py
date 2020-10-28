import os
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def indexView(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def pwResetView(request):
	template = loader.get_template('pwReset_auth.html')
	context = {}
	return HttpResponse(template.render(context, request))
