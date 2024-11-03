from django.urls import path
from .views import AddFavoriteView, FavoriteDetailView, FavoriteListView

urlpatterns = [
    path('add/', AddFavoriteView.as_view(), name='add_favorite'),  # Create
    path('getall/<int:id>/', FavoriteListView.as_view(), name='favorite_list'),   # List
    path('findone/<int:id>/', FavoriteDetailView.as_view(), name='favorite_detail'), 
]
