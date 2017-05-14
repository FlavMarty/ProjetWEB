from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tableaubord,name='tableaubord'),
    url(r'^sign1/$', views.sign1,name='sign1'),
    url(r'^createEvent/$', views.createEvent,name='createEvent'),
    url(r'^deleteEvt/(?P<id>\d+)$', views.deleteEvent,name='deleteEvent'),
]
