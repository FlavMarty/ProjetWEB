from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.evenement),
    url(r'^events/(?P<id>\d+)$', views.detailevenement,name='detailEvenement'),
    url(r'^dislikeEvt/(?P<id>\d+)$', views.dislikeEvent,name='dislikeEvent'),
]
