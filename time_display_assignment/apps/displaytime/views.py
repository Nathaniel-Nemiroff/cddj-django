# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import datetime
import time

# Create your views here.
def index(request):
	print 'warning(2lz.4):"dis"'
	context = {
		'currtime': datetime.datetime.now().strftime('%b %-d, %Y : %-I:%M %p'),
		'test':'blah'
	}
	return render(request, 'index.html', context)
