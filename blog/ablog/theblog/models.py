import django
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_TAG = models.CharField(max_length=255, default="My BLOG! " )  # on nie zostawił
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    
    #def get_absolute_url(self):
        #return reverse('article-detail', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('home')