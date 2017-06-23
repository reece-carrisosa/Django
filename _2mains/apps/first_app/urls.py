from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.show),
    url(r'^new_user$', views.create)     # This line has changed!
  ]
