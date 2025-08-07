from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),


    #path('',views.index),
    #path('<int:pk>/', views.detail),
    #path('create/', views.create),
    #path('<int:pk>/delete/', views.delete),
    #path('<int:pk>/update/', views.update),

    path('<int:pk>/createComment/', views.createComment, name='createComment'),
    path('<int:pk>/updateComment/', views.updateComment, name='updateComment'),
    path('<int:pk>/deleteComment/', views.deleteComment, name='deleteComment'),
    path('category/<slug>/', views.category),
    path('createfake/', views.createfake),
]