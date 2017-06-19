# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import random

# Create your views here.
def index(request):
	if request.method == 'GET':
		request.session['hits']=1
	else:
		request.session['hits']+=1
	context={
		'value':random.randrange(0,1000000000),
		'hit':request.session['hits']
	}
	return render(request, 'index.html',context)
