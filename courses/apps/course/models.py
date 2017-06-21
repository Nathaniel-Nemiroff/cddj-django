# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def getCourses(self):
		return Course.objects.all()
	def getCourse(self, id):
		return Course.objects.get(id=id)

	def addCourse(self, postData):
		if(postData['name'] and postData['desc']):
			Course.objects.create(name=postData['name'], 
													  desc=postData['desc'])

	def destroyCourse(self, postData):
		Course.objects.filter(id=postData).delete()

class Course(models.Model):
	name = models.CharField(max_length=38)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = CourseManager()
