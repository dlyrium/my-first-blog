from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/unpub/', views.post_unpub, name='post_unpub'),
    path('post/<int:pk>/publish/', views.post_publish, name="post_publish"),
    path('post/<int:pk>/remove/', views.post_remove, name="post_remove"),
    path('post/<int:pk>/comment/', views.comment_add, name="comment_add"),
    path('post/<int:pk>/comment_approve/',
         views.comment_approve, name="comment_approve"),
    path('post/<int:pk>/comment_remove/',
         views.comment_remove, name="comment_remove"),
]
