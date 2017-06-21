from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^wall$', views.wall),
	url(r'^newmsg',views.newmsg),
	url(r'^newcmnt',views.newcmnt)
]
