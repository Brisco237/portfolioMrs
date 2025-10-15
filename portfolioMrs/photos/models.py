from django.db import models

# Create your models here.
class Photos(models.Model):
    image = models.ImageField(upload_to='media/photos')
    title = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    technique = models.TextField(max_length=1000)
    size = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)