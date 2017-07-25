from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_npc(?:Class=(?P<classname>\d+)/)?(?:Race=(?P<race>\d+)/)?(?:Subrace=(?P<subrace>\d+)/)?$', views.create_npc, name='create_npc'),
]