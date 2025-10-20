from django.contrib import admin
from .models import Photos,Categorie

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Photos)

admin.site.site_title = "Espace Administrateur"
admin.site.site_header = "Bienvenue Mr.S"