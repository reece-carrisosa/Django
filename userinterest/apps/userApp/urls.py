from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users),
    url(r'^interests$', views.interests),
    url(r'^view/(?P<id>\d+)$', views.view)
]