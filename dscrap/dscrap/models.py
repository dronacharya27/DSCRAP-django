from django.db import models
from .apps import user_directory_path

class contact(models.Model):
    name = models.CharField(max_length=50,default='',primary_key=True,unique=False)
    email=models.CharField(max_length=50,default='')
    subject = models.CharField(max_length=50,default='')
    message = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=64,default='')
    image = models.ImageField(upload_to=user_directory_path) 

class useraddress(models.Model):
    username = models.CharField(max_length=50,default='')
    add = models.CharField(max_length=500,default='')