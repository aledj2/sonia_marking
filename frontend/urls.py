from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.SelectClass, name='SelectClass'),
    url(r'^add_marking/(?P<classid>[0-9]+)/$',views.AddMarking,name='add_marking'),
    #url(r'^ViewClass/$',views.SelectClass,name='SelectClass'),
]