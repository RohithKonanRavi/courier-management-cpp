from django.urls import path, re_path
from . import views

urlpatterns = [
    path('tracking-record', views.trackinglisting, name="trackinglisting"),
    path('tracking-search', views.trackingsearch, name="trackingsearch"),
    re_path(r'^tracking-add/(?P<goodsId>[\w-]{0,50})/$', views.add, name="add"),
    re_path(r'^tracking-update/(?P<trackingId>[\w-]{0,50})/$', views.update, name="update"),
    re_path(r'^tracking-delete/(?P<id>\w{0,50})/$', views.delete, name="delete"),
    # re_path(r'^tracking-delete/(?P<trackingId>\w{0,50})/$', views.delete, name="delete"),
]