from django.db import models

# Create your models here.
class Userdata(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=16)
    