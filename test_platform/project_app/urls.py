from django.urls import path
from django.shortcuts import render
from project_app import views

urlpatterns = [
    path('project_manage/', views.project_manage),
]
