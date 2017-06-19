# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def ninjas(request, color):

	colors = {
		'blue':'img/leonardo.jpg',
		'orange':'img/michelangelo.jpg',
		'red':'img/raphael.jpg',
		'purple':'img/donatello.jpg',
	}

	if not color:
		color = 'img/tmnt.png'
	elif color in colors:
		color = colors[color]
	else:
		color = 'img/notapril.jpg'
		
	context = {
		'file' : color
	}
	return render(request, 'ninjas.html', context)
