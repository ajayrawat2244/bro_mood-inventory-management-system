from django.contrib import admin
from django.urls import path
from room import views

urlpatterns = [
    path("",views.index, name='index'),
    path("sections",views.sections, name='sections'),
    path("sale", views.sale, name= 'sale    ')
]
