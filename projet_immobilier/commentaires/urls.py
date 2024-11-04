from django.urls import path
from .views import  CommentaireListCreateAPIView


urlpatterns = [
    path('', CommentaireListCreateAPIView.as_view(), name='commentaire-list-create'),
    path('<int:id>', CommentaireListCreateAPIView.as_view(), name='commentaire-detail'),
]