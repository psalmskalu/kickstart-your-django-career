from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "sample_app"

urlpatterns = [

    path('', views.index, name = 'index'),
    path('add/', views.add, name = 'add'),
    
]