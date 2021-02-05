from django.urls import path, include
from .views import orderDisplay
urlpatterns = [
    path('',orderDisplay)
]