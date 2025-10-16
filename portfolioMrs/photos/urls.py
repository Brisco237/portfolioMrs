from django.urls import path
from .views import store, about

urlpatterns = [
    path('store/', store, name="store"),
    path('about/', about, name="about"),
]
