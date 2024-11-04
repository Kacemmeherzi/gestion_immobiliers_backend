from rest_framework import serializers
from .models import Commentaire

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ['id', 'annonce', 'user', 'contenu', 'date_creation']
        read_only_fields = ['date_creation']
