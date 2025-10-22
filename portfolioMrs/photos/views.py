from django.shortcuts import render
from .models import Photos
from django.views.generic import ListView, DetailView

# Create your views here.
class PhotoListView(ListView):
    model = Photos
    template_name = 'photos/store.html'
    context_object_name = 'photos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_queryset().count()
        return context

class PhotoDetailView(DetailView):
    model = Photos
    template_name = 'photos/dessin_detail.html'
    context_object_name = 'photo'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

def about(request):
    return render(request, 'portfolioMrs/about.html')

def contact(request):
    return render(request, 'portfolioMrs/contact.html')