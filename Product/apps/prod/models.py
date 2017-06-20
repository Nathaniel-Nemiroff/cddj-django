# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Products(models.Model):
	name = models.CharField(max_length=38)
	description = models.TextField()
	weight = models.IntegerField()
	price = models.IntegerField()
	cost = models.IntegerField()
	category = models.CharField(max_length=38)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
