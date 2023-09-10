from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home , name='home'),
    path('tasks/', views.tasks , name='tasks'),
    path('tasks/deleteTask/', views.deleteTask, name='deleteTask'),
    path('tasks/deleteAllTasks/',views.deleteAllTasks, name='deleteAllTasks'),
    path('tasks/updateTask', views.updateTask, name='updateTask')
]
