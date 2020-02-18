from django.db import models
from django.contrib.auth.models import User
from TwitterClone.tweets.models import Tweet
from TwitterClone.twitterusers.models import TwitterUser

class Notification(models.Model):
     tweetfrom = models.ForeignKey(Tweet,on_delete=models.CASCADE)
     tweetfor = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
     
     def __str__(self):
        return f"{self.tweetfrom}-{self.tweetfor}"