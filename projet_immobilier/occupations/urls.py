from django.urls import path
from .views import create_occupation, get_all_occupations, get_occupations_by_client, get_occupations_by_owner

urlpatterns = [
    path('client/<int:user_id>/', get_occupations_by_client, name='get_occupations_by_client'),
    path('owner/<int:user_id>/', get_occupations_by_owner, name='get_occupations_by_owner'),
    path('all/', get_all_occupations, name='get_all_occupations'),
    path('create',create_occupation , name='get_all_occupations'),

]
