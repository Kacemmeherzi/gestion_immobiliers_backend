from django.shortcuts import render

from rest_framework import viewsets

from .models import Commentaire
from .serializers import CommentaireSerializer

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
   # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Ajoute l'utilisateur connecté comme auteur du commentaire
        serializer.save(user=self.request.user)
