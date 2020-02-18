from django.db import models
from django.contrib.auth.models import User
from TwitterClone.twitterusers.models import TwitterUser
from django.utils import timezone

class Tweet(models.Model):
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     content = models.TextField(max_length=150)
     created = models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return f"{self.author}-{self.content}-{self.created}"