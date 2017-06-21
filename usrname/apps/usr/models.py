# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def getUsers(self):
		return User.objects.all()

	def addUser(self, postData):
		if User.objects.filter(email=postData+'@codingdojo.com').exists():
			print 'false'
			return False
		print 'true'
		User.objects.create(email=postData+'@codingdojo.com')
		return True

class User(models.Model):
	email = models.CharField(max_length=38)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
