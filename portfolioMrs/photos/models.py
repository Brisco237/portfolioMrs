from django.db import models
from django.utils.text import slugify

# Create your models here.
class Categorie(models.Model):
    title = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'catégorie'
        verbose_name_plural = 'catégories'

    def __str__(self):
        return self.title
    
class Photos(models.Model):
    image = models.ImageField(upload_to='photos/')
    slug = models.SlugField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='photos',null=True,blank=True)
    title = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    technique = models.TextField(max_length=100)
    size = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Photos.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title