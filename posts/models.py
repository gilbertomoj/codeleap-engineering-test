from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    username = models.CharField(max_length=30)
    created_datetime = models.DateTimeField(auto_now_add=True)
