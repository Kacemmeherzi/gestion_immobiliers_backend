from django.urls import path
from .views import create_annonce, delete_annonce, get_annonce ,get_all_annonces

urlpatterns = [
   path('create', create_annonce, name='create_annonce'),
    path('findone/<int:pk>/', get_annonce, name='get_annonce'),
    path('delete/<int:pk>/', delete_annonce, name='delete_annonce'),
    path('getall', get_all_annonces, name='delete_annonce'),

]
