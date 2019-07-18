from django.contrib import admin
from django.urls import path
from .views import index,weather_view

urlpatterns = [
    path('', index),
    path('weather',weather_view),
]