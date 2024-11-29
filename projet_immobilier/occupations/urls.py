from django.urls import path
from .views import create_occupation, get_all_occupations, get_occupations_by_client, get_occupations_by_owner,accept_occupation,get_occupations_by_annonce

urlpatterns = [
    path('client/<int:user_id>/', get_occupations_by_client, name='get_occupations_by_client'),
    path('owner/<int:user_id>/', get_occupations_by_owner, name='get_occupations_by_owner'),
    path('all/', get_all_occupations, name='get_all_occupations'),
    path('create',create_occupation , name='get_all_occupations'),
    path('activate/<int:id>/',accept_occupation, name='get_all_occupations'),
    path('getallbyannonce/<int:annonceid>/',get_occupations_by_annonce, name='get_all_occupations'),



]
