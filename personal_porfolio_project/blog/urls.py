from django.urls import path
from . import  views

urlpatterns = [

    path('',views.home_blog, name="home_blog"),
 ]