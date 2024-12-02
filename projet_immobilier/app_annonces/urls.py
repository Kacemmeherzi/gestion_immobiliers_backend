from django.urls import path
from .views import create_annonce, delete_annonce, get_annonce ,get_all_annonces ,get_all_annonces_by_owner

urlpatterns = [
   path('create', create_annonce, name='create_annonce'),
    path('findone/<int:pk>/', get_annonce, name='get_annonce'),
    path('delete/<int:pk>/', delete_annonce, name='delete_annonce'),
    path('getall', get_all_annonces, name='delete_annonce'),
    path('getbyowner/<int:id>/', get_all_annonces_by_owner, name='byowner'),


]
