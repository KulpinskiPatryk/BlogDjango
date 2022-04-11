from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique_for_date='dateOfPublish')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    dateOfPublish = models.DateTimeField(default=timezone.now)
    dateOfCreated = models.DateTimeField(auto_now_add=True)
    dateOfUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-dateOfPublish']

    def __str__(self):
        return self.title


# Create your models here.
