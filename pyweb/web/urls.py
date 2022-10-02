from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('',views.home, name="home"),
    path('home',views.home, name="Libaray Portal"),
    path('Class',views.Class, name="Select"),
    path('Know_more',views.Know_more, name="Know_more"),
    path('Contact_us',views.Contact_us, name="Contact_us"),
    path('login_page',views.login_page, name="Login"),
    path('firstpage',views.firstpage, name="firstpage"),
]