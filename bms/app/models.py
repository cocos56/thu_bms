from django.db import models

# Create your models here.


class Book(models.Model):
    # id = models.IntegerField() # 自动创建
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    price = models.FloatField()
    number = models.IntegerField()
