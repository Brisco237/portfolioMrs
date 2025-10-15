from django.shortcuts import render
from photos.models import Photos

def home(request):
    photos = Photos.objects.all()
    return render(request, 'portfolioMrs/home.html', {'photos':photos})