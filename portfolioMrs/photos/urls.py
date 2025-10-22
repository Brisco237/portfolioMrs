from django.urls import path
from .views import PhotoListView, PhotoDetailView, about, contact

urlpatterns = [
    path('', PhotoListView.as_view(), name='store'),
    path('Dessin/<slug:slug>/', PhotoDetailView.as_view(), name='dessin_detail'),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact")
]
