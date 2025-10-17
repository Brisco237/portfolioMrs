from django.urls import path
from .views import store, about, contact

urlpatterns = [
    path('store/', store, name="store"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact")
]
