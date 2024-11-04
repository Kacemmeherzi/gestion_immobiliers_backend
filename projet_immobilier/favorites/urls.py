from django.urls import path
from favorites.views import FavoriteView

urlpatterns = [
    path('', FavoriteView.as_view(), name='favorite-list'),  # List and Create
    path('<int:id>', FavoriteView.as_view(), name='favorite-detail'),
]
