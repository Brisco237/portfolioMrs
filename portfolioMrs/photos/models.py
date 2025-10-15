from django.db import models

# Create your models here.
class Photos(models.Model):
    image = models.ImageField(upload_to='photos/')
    title = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    technique = models.TextField(max_length=100)
    size = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        return self.title