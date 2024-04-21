from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="login"),
    re_path(r'^dashboard$', views.listing, name="listing"),
    re_path(r'^forgot$', views.forgot, name="forgot"),
    re_path(r'^logout$', views.logout, name="logout"),
    re_path(r'^changepassword$', views.changepassword, name="changepassword"),
    path('register', views.register, name='register'),  # New URL pattern for the registration page
    
]