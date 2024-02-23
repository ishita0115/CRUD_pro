from django.db import models
from django.utils import timezone

# Create your models here.

class Record(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length = 255)
    phone=models.IntegerField()
    city = models.CharField(max_length=300)

    def __str__(self):
        return self.first_name + "   " + self.last_name