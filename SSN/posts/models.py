from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}, {self.body[:30]}'

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk': self.id})
