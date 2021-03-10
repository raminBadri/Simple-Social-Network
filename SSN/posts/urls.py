from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_list_view, name='all-posts'),
]
