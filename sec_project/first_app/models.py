from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=264, unique=True)
    surname = models.CharField(max_length=264, unique=True)
    mail = models.EmailField(max_length=264)

    def __str__(self):
        return self.name