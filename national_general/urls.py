'''
Created on Apr 8, 2017

@author: roadd
'''
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^statistics/general/$', views.general, name='general'),
    url(r'^statistics/agegroup/$', views.agegroup, name='agegroup'),
]
