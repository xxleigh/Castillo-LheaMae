from django.db import models

# Create your models here.

# models.py
from django.db import models

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # Images will be uploaded to 'media/images/'

    def __str__(self):
        return self.title

from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
