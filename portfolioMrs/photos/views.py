from django.shortcuts import render
from .models import Photos

# Create your views here.
def store(request):
    photos = Photos.objects.all()
    total  = Photos.objects.count()
    return render(request, 'photos/store.html', {'photos' : photos, 'total' : total})

def about(request):
    return render(request, 'portfolioMrs/about.html')

def contact(request):
    return render(request, 'portfolioMrs/contact.html')