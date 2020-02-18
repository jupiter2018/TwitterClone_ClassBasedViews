from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     following = models.ManyToManyField("self",blank=True, symmetrical=False)
     def __str__(self):
        return f"{self.user}-{self.following}"


    