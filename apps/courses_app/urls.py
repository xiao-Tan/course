from django.conf.urls import url
from . import views   

urlpatterns = [ 
    url(r'^$', views.index),
    url(r'^courses/destory/(?P<num>\d+)$', views.destory),
    url(r'^courses/destory', views.delete),
    url(r'^courses/(?P<num>\d+)/comment$', views.comment),
]