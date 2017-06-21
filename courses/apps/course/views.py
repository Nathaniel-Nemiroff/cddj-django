# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import Course

# Create your views here.
def index(request):
	context = { 'courses':Course.objects.getCourses() }
	return render(request, 'index.html', context)

def addCourse(request):
	if request.method == 'POST':
		Course.objects.addCourse(request.POST)
	return redirect('/')

def destroy(request, id):
	c = Course.objects.getCourse(id)
	context = { 
		'id':c.id,
		'name':c.name,
		'desc':c.desc
	 }
	return render(request, 'destroy.html',context)

def destroyconfirm(request, id):
	Course.objects.destroyCourse(id)
	return redirect('/')
