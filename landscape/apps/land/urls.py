from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<val>\w*)$', views.index)
]
