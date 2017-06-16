from django.conf.urls import url
from .import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^a$', views.index2),
	url(r'^testimonials$', views.testimonials),
	url(r'^projects$', views.proj),
	url(r'^about$', views.about)
]
