from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^secrets$', views.secrets),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^post$', views.post),
	url(r'^like$', views.like, name="like"),
	url(r'^delete$', views.delete),
	url(r'^confirmdelete$', views.confirmdelete)
]
