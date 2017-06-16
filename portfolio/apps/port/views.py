# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'port/index.html')

def index2(request):
	return render(request, 'index.html')

def testimonials(request):
	return render(request, 'port/testimonials.html')

def proj(request):
	if request.method == 'GET':
		return redirect('/')
	print '---'
	print request.POST
	print request.method
	print '---'
	return render(request, 'port/proj.html')

def about(request):
	return render(request, 'port/about.html')
