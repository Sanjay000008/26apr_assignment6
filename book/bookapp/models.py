from django.db import models

# Create your models here.
class books(models.Model):
    title=models.CharField(max_length=50)
    auther=models.CharField(max_length=50)
    isbn=models.CharField(max_length=17)
    publisher=models.CharField(max_length=50)