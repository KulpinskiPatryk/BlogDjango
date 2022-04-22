from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce import models as tm_models
from taggit.managers import TaggableManager


class contactForm(models.Model):
    formEmail = models.EmailField()
    formMessage = models.TextField()

    def __str__(self):
        return self.formEmail + ' ' + self.formMessage


class beforeUser(models.Model):
    userName = models.TextField(unique=True)
    userPassword = models.TextField()
    userEmail = models.EmailField(unique=True)
    userActive = models.IntegerField(default=0)


    def __str__(self):
        return self.userName + ' ' + self.userEmail + ' ' + str(self.userActive)


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True, unique_for_date='dateOfPublish')
    body = tm_models.HTMLField()
    image = models.ImageField(upload_to='images/', null=False,blank=False)
    dateOfPublish = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    class Meta:
        ordering = ['-dateOfPublish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:singlePost', args=[self.slug])


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, default='Anonymous')
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body

# Create your models here.
