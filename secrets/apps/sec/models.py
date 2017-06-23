# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models import Count

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def addUser(self, postData):
		if not ( postData['first'] and postData['last'] and
						 postData['email'] and postData['pswd'] and
						 postData['conf']):
			return 'Must fill all fields!'
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

		if not User.objects.filter(email=postData['email']):
			User.objects.create(first_name=postData['first'],
													last_name=postData['last'],
													email=postData['email'],
													password=postData['pswd'])
		else:
			return 'User exists!'

		return 'Success!'
		
	def getUser(self, postData):
		if not ( postData['email'] and postData['pswd']):
			return False
		if not User.objects.filter(email=postData['email']):
			return False
		user=User.objects.get(email=postData['email'])
		if not user.password == postData['pswd']:
			return False

		return user


class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=255)
	salt = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

class SecretManager(models.Manager):
	def addSecret(self, postData, userid):
		if not postData['secret']:
			return False
		Secret.objects.create(message=postData['secret'], user=User.objects.get(id=userid))
	def removeSecret(self, postData):
		if Secret.objects.filter(id=postData):
			Secret.objects.get(id=postData).delete()
	def addLike(self, postData, userid):
		S = Secret.objects.get(id=postData['secret'])
		if not User.objects.filter(id=userid, likes=S):
			S.likes.add(User.objects.get(id=userid))
			S.likenum+=1
			S.save()
		pass
	def getRecent(self):
		return Secret.objects.all().order_by('-created_at')[:10]
	def getPopular(self):
		return Secret.objects.order_by('-likenum')
	
class Secret(models.Model):
	message = models.TextField()
	user = models.ForeignKey(User, related_name="secrets")
	likes = models.ManyToManyField(User, related_name='likes')
	likenum = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = SecretManager()
