from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:pk>/', views.detail),
    path('create/', views.create),
    path('createfake/', views.createfake),
    path('category/<slug>/', views.category),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/update/', views.update),
    path('<int:pk>/createComment/', views.createComment, name='createComment'),
    path('<int:pk>/updateComment/', views.updateComment, name='updateComment'),
    path('<int:pk>/deleteComment/', views.deleteComment, name='deleteComment'),


]