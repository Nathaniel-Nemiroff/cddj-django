# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	#response = "hello, this is a request"
	print "*"*50
	return render(request, 'first_app/index.html')#HttpResponse(response)

def temp(request):
	print request.method
	return render(request, 'first_app/temp.html')
