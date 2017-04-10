from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^graphics$', views.graphics, name='graphics'),
    url(r'^text$', views.text, name='text'),
    url(r'^demografia$', views.demografia, name='demografia'),
    url(r'^tranzitia$', views.tranzitia, name='tranzitia'),
    url(r'^istoric$', views.istoric, name='istoric'),
    url(r'^donatii$', views.donatii, name='donatii'),
]
