from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) # If user is deleted, also delete all related posts

    def __str__(self):
        return self.title

    # reverse: return full url as a string, let view handle redirect
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
