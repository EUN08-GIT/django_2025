from django.urls import path
from . import views

urlpatterns = [
    path('',views.library),
    path('<int:pk>/', views.detail),
    path('create/', views.create)
]