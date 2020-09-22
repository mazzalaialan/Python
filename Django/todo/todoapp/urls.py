from django.contrib import admin
from django.urls import path
from .views import todoview, addtask, deletetask, edittask, updatetask

urlpatterns = [
    path('', todoview, name='homepage'),
    path('addtask/', addtask),
    path('deletetask/<int:taskpk>/', deletetask),
    path('updatetask/<int:taskpk>/', edittask),
    path('updatetask/<int:taskpk>/update/', updatetask),
]
