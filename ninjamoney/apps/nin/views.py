# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

import random

# Create your views here.
def index(request):
	if 'gold' not in request.session:
		request.session['gold']=0
	if 'log' not in request.session:
		request.session['log']=''
	
	context = {
		'gold':str(request.session['gold']),
		'log':request.session['log']
	}
	return render(request, 'nin/ninjamoney.html', context)

def proc(request):
	if not request.method == 'POST':
		return redirect('/')

	switch = {
		'farm':random.randrange(9, 21),
		'cave':random.randrange(4, 11),
		'house':random.randrange(1, 6),
		'casino':random.randrange(-51, 51)
	}
	gold = switch[request.POST['building']]
	request.session['gold']+=gold
	request.session['log']+="Earned "+str(gold)+" gold from the "
	request.session['log']+=request.POST['building']+"!\n"
	

	return redirect('/')


def reset(request):
	if not request.method == 'POST':
		redirect('/')
	del request.session['gold']
	del request.session['log']
	return redirect('/')
