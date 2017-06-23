# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import User

# Create your views here.
def index(request):
	context = {}
	if 'flash' in request.session:
		context['flash']=request.session['flash']
		request.session.pop('flash')
	return render(request, 'index.html', context)

def register(request):
	if not request.method=='POST':
		return redirect('/')

	msg=User.objects.addUser(request.POST)
	if not msg:
		request.session['name']=request.POST['first']
		return redirect('/success')

	request.session['flash']=msg
	return redirect('/')

def login(request):
	if not request.method=='POST':
		return redirect('/')

	if User.objects.getUser(request.POST):
		request.session['name']=User.objects.filter(email=request.POST['email'])[0].first_name
		print request.session['name']
		return redirect('/success')

	request.session['flash']=msg
	return redirect('/')


def success(request):
	context = {}
	if 'name' in request.session:
		context = { 'name':request.session['name'] }
		request.session.pop('name')
	return render(request, 'success.html', context)
