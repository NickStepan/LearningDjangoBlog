from django.urls import path
from . import views

urlpatterns = [
    path('post-list', views.post_list, name="post-list"),
    path('post/<int:pk>', views.post_details, name="post"),
    path('author_posts/<int:pk>', views.author_posts, name="posts") 
]