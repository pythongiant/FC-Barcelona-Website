from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)

    Name = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    Description = models.TextField()
    ProfilePic = models.FileField()

    def __str__(self):
        return self.Name.username
class Posts(models.Model):
    
    id = models.IntegerField(primary_key=True,unique=True)
    Name = models.CharField(max_length=255)
    post = models.TextField()
    author = models.ForeignKey('Person', on_delete=models.CASCADE)
    def __str__(self):
        return self.Name 
