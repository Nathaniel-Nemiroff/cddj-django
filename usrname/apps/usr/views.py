# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import User

# Create your views here.
def index(request):
	context = { 'users':User.objects.getUsers() }

	if request.method=='POST':
		if User.objects.addUser(request.POST['usr']):
			context['success']=True
		else:
			context['fail']=True
	print context

	return render(request, 'index.html',context)

def validate(request):
	#if request.method=='POST':
		#if User.objects.addUser(request.POST['usr']):
			
	return redirect('/')
