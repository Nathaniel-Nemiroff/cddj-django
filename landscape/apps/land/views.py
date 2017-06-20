# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from math import floor
from random import randrange

# Create your views here.
def index(request,val):
	chk=True
	fil = "blah"
	prime=True
	if not val:
		chk=False
	else:
		for i in range(2, int(floor((float(val)/2)))):
			if float(val)/i % 1 == 0:
				val=floor((float(val)-1)/10)
				prime=False
				break
		if prime:
			val=randrange(0,4)

	files = {
		0:'img/snow.jpg',
		1:'img/desert.png',
		2:'img/forrest.jpg',
		3:'img/farm.jpg',
		4:'img/beach.png'
	}
	if val in files:
		fil=files[val]
	else:
		chk=False

	context ={
		'chk':chk,
		'file':fil
	}
	return render(request, 'index.html',context)
