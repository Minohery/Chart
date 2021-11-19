from django.urls import path, include
from . import views

app_name='todo'

urlpatterns=[
    path('add/', views.add, name="add"),
    path('liste/', views.liste, name="liste"),
    path('delete/<int:num>/', views.delete, name="delete"),
    path('draw/', views.draw, name="draw"),
]
