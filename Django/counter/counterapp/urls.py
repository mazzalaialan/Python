from django.contrib import admin
from django.urls import path
from .views import home,increment,decrement,reset

urlpatterns = [
    path('', home),
    path('increment/', increment),
    path('decrement/', decrement),
    path('reset/', reset),
]
