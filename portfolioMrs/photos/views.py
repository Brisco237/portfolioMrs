from django.shortcuts import render
from .models import Photos

# Create your views here.
def store(request):
    photos = Photos.objects.all()
    return render(request, 'photos/store.html', {'photos' : photos})