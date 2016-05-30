from django.db import models
from  django.utils import timezone
from django.forms import widgets
# Create your models here.

class Lunchrequest(models.Model):
    user = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    time = models.DateTimeField()
    email = models.EmailField()


    def __str__(self):
        return self.user
