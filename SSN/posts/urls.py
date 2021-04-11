from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_list_view, name='all-posts'),
    path('post-detail/<int:pk>', views.post_detail, name='post-detail'),
]
