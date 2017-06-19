# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'surv/index.html')

def process(request):
	if request.method == 'POST':
		request.session['name']=request.POST['name']
		request.session['loc']=request.POST['loc']
		request.session['lan']=request.POST['lan']
		request.session['comm']=request.POST['comm']


		if not 'hits' in request.session:
			request.session['hits']=1
		else:
			request.session['hits']+=1

		return redirect('/results')
	return redirect('/')

def result(request):
	#if not request.method == 'POST':
		#return redirect('/')
	print request.session
	if 'name' not in request.session:
		return redirect('/')


	context={
		'name': request.session['name'],
		'loc': request.session['loc'],
		'lan': request.session['lan'],
		'comm': request.session['comm'],
		'hits': request.session['hits']
	}
	del request.session['name']

	return render(request, 'surv/result.html', context)
