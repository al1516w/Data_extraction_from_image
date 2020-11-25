from django.db import models
import os

# Create your models here.


class Imagee(models.Model):
    pic = models.ImageField(upload_to='pictures')
