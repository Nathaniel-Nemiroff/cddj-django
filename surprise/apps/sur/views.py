# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

import random

VALUES = ['hello', 'world', 'hello world', 'sna', 'foo', 'snafoo', 'foo', 'bar', 'foobar']

# Create your views here.
def index(request):
	#shuffle...
	return render(request, 'index.html')
def results(request):	
	if not request.method == 'POST':
		return redirect('/')
	if not request.POST['val'].isdigit():
		return redirect('/')

	items=''
	random.shuffle(VALUES)
	for i in range(0, min(int(request.POST['val']),9)):
		items+= VALUES[i]+'\n'
	context={
		'items':items
	}
	return render(request, 'results.html', context)
