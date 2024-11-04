from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentaireViewSet

urlpatterns = [
    path('add/', CommentaireViewSet.as_view(), name='add_commentaire'),  # Create
   
]
