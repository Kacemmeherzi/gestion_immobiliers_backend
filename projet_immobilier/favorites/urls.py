from django.urls import path
from favorites.views import    create_favorite , delete_favorite, get_favorites_by_user

urlpatterns = [
    path('getfavorite/<int:id>',get_favorites_by_user, name='getfavbyuserid'),
    path('delete/<int:id>', delete_favorite, name='deletefavortie'),
    path('create', create_favorite, name='create'),


]
