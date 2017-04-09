'''
Created on Apr 8, 2017

@author: roadd
'''
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^statistics/general/$', views.general, name='general'),
    url(r'^statistics/general/agegroup/$', views.agegroup, name='agegroup'),
    url(r'^statistics/general/year/$', views.year, name='year'),
    url(r'^statistics/general/natality/$', views.natality, name='natality'),
    url(r'^statistics/general/fertility/$', views.fertility, name='fertility'),
    url(r'^statistics/general/aborts/$', views.aborts, name='aborts'),
    url(r'^statistics/general/naturalincrease/$', views.naturalincrease, name='naturalincrease'),
    url(r'^statistics/general/marriage/$', views.marriage, name='marriage'),
    url(r'^statistics/general/deaths/mortality/$', views.mortality, name='mortality'),
    url(r'^statistics/general/deaths/abortdeaths/$', views.abortdeaths, name='abortdeaths'),
    url(r'^statistics/general/deaths/infantdeaths/$', views.infantdeaths, name='infantdeaths'),
    url(r'^statistics/general/deaths/borndead/$', views.borndead, name='borndead'),
]
