# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import User, Secret

# Create your views here.

'''



Add delete function









'''

def index(request):
	context={}
	if 'flash' in request.session:
		context['flash']=request.session['flash']
		request.session.pop('flash')
	if 'user' in request.session:
		context['user']=User.objects.get(id=request.session['id'])
	else:
		context['user']=False

	context['secrets']=Secret.objects.getRecent()

	return render(request, 'index.html', context)

def secrets(request):
	context={'secrets':Secret.objects.getPopular()}
	if 'user' in request.session:
		context['user']=User.objects.get(id=request.session['id'])
	return render(request, 'secrets.html', context)

def register(request):
	if request.method == 'POST':
		request.session['flash']=User.objects.addUser(request.POST)
	return redirect('/')

def login(request):
	if request.method=='POST':

		user = User.objects.getUser(request.POST)
		if not user:
			request.session['flash']='Login Failed!'
		else:
			request.session['user']=str(user.first_name)
			request.session['id']=user.id

	return redirect('/')

def logout(request):
	if request.method=='POST':
		if('user' in request.session):
			request.session.pop('user')
		if('id' in request.session):
			request.session.pop('id')
	return redirect('/')

def post(request):
	if request.method=='POST':
		if request.session['user']:
			Secret.objects.addSecret(request.POST, request.session['id'])

	return redirect('/')

def delete(request):
	print 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa'
	if request.method=='POST':
		print 'bluh'
		if request.session['user']:
			request.session['delete']=request.POST['delete']
			context = { 'secret':Secret.objects.get(id=request.POST['delete'])}
			return render(request, 'delete.html', context)
	return redirect('/')

def confirmdelete(request):
	if request.method=='POST':
		Secret.objects.removeSecret(request.session['delete'])
		request.session.pop('delete')
	return redirect('/')

def like(request):
	if request.method=='POST':
		if request.session['user']:
			Secret.objects.addLike(request.POST, request.session['id'])
	return redirect('/')
