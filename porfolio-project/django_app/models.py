from django.db import models

# Create your models here.
class Django_app(models.Model):
    #images
    image = models.ImageField(upload_to='images/')
    #sumary
    sumary = models.CharField(max_length=200)
    