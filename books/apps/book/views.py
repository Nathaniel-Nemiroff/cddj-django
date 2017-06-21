# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Books

# Create your views here.
def index(request):
	context = { 'books' : Books.objects.getTitles() }
	return render(request, 'index.html', context)

def addbook(request):
	if request.method == 'POST':
		Books.objects.addBook(request.POST)
	return redirect('/')

#add and retrive info and display books
#title category author
