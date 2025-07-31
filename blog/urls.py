from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:pk>/', views.detail),
    path('create/', views.create),
    path('createfake/', views.createfake)

]