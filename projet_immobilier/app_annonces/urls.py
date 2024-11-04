from django.urls import path
from .views import AnnonceListCreate, AnnonceDetail

urlpatterns = [
    path('', AnnonceListCreate.as_view(), name='annonce-list-create'),
    path('annonces/<int:pk>/', AnnonceDetail.as_view(), name='annonce-detail'),
]
