# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def addUser(self, postData):
		if( postData['first'] and postData['last'] and
				postData['email'] and postData['pswd'] and
				postData['conf']):
			if(len(postData['first'])<2 or len(postData['last'])<2):
				return 'Name must have more than 1 character!'
			if(not NAME_REGEX.match(postData['first']) or
				 not NAME_REGEX.match(postData['last'])):
				return 'Name must not contain numbers!'
			if(not EMAIL_REGEX.match(postData['email'])):
				return 'Email not valid!'
			if(len(postData['pswd'])<8):
				return 'Password must be at least 8 characters!'
			if not postData['pswd'] == postData['conf']:
				return 'Passwords must match!'

			User.objects.create(first_name=postData['first'], 
													last_name=postData['last'], 
													email=postData['email'], 
													password=postData['pswd'])
			return False

		else:
			return 'Must fill all feilds!'

	def getUser(self, postData):
		if( postData['email'] and postData['pswd'] ):
			u = User.objects.filter(email=postData['email'])
			if u.exists():
				if u[0].password == postData['pswd']:
					return True

		return False

class User(models.Model):
	first_name = models.CharField(max_length=38)
	last_name = models.CharField(max_length=38)
	email = models.CharField(max_length=38)
	password = models.CharField(max_length=38)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
