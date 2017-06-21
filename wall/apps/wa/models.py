# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
	first_name = models.CharField(max_length=38)
	last_name = models.CharField(max_length=38)
	email = models.CharField(max_length=60)
	password = models.CharField(max_length=100)
	salt = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class messages(models.Model):
	user_id = models.ForeignKey(users)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class comments(models.Model):
	message_id = models.ForeignKey(messages)
	user_id = models.ForeignKey(users)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
