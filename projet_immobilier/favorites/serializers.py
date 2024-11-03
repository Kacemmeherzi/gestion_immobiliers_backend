# serializers.py
from rest_framework import serializers

from app_annonces.serializers import AnnonceSerializer
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    annonce = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'annonce', 'created_at']
    def get_annonce(self, obj):
        # You can add logic here to return just the annonce details or a link to expand
        return AnnonceSerializer(obj.annonce).data
       