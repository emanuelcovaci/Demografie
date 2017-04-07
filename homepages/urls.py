from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^graphics', views.graphics, name='graphics'),
    url(r'^text', views.text, name='text'),
    url(r'^dash', views.dash, name='dash'),
]
