from django.db import models
from datetime import timedelta
from django.utils import timezone




# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, default=None, related_name='post')

    def published_recently(self):
        return timezone.now() - timedelta(days=7) < self.published_date

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None, related_name='comments')
    author_name = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author_name}, {self.post}"



