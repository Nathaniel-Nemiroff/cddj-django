from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^addcourse$', views.addCourse),
	url(r'^destroy/(?P<id>\d+)$', views.destroy),
	url(r'^destroyconfirm(?P<id>\d+)$', views.destroyconfirm)
]
