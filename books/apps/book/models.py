# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BooksManager(models.Manager):
	def myfun(self, postData):
		print '-----------------------------------'
		print 'muh login m8'
		print postData
		print '-----------------------------------'

	def getTitles(self):
		return Books.objects.all()

	def addBook(self, postData):
		if (postData['title'] and postData['author']
			and postData['category']):
			print 'success!'
			Books.objects.create(title=postData['title'],
													 author=postData['author'],
													 category=postData['category'])
			


class Books(models.Model):
	title = models.CharField(max_length=38)
	author = models.CharField(max_length=38)
	category = models.CharField(max_length=38)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = BooksManager()
